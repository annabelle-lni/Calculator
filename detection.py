import os
import cv2
import numpy as np

def load_templates(numbers_path, signs_path):
    templates = {}

    for i in range(10):
        template_path = os.path.join(numbers_path, f"num{i}.jpg")
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is not None:
            templates[str(i)] = template
        else:
            print(f"Error: {template_path} not found or unreadable.")

    operations = {"add": "+", "sub": "-", "mult": "*", "div": "/"}
    for key, symbol in operations.items():
        template_path = os.path.join(signs_path, f"{key}.jpg")
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is not None:
            templates[symbol] = template
        else:
            print(f"Error: {template_path} not found or unreadable.")

    if not templates:
        print("No valid templates loaded.")
    return templates

def compare_with_templates(extracted_img, templates):
    best_match = None
    max_val = 0

    for key, template in templates.items():
        extracted_img_resized = cv2.resize(extracted_img, (template.shape[1], template.shape[0]))
        result = cv2.matchTemplate(extracted_img_resized, template, cv2.TM_CCOEFF_NORMED)
        _, max_val_current, _, _ = cv2.minMaxLoc(result)

        if max_val_current > max_val:
            best_match = key
            max_val = max_val_current

    return best_match

def process_image(image, numbers_path, signs_path):
    if len(image.shape) != 2 or np.max(image) > 255 or np.min(image) < 0:
        print("The image is not binary.")
        return

    templates = load_templates(numbers_path, signs_path)
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    expression = []
    elements = []

    for contour in contours:
        if cv2.contourArea(contour) < 100:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        roi = image[y:y+h, x:x+w]
        match = compare_with_templates(roi, templates)

        color = (0, 0, 255) if isinstance(match, int) else (255, 0, 0)
        cv2.rectangle(output_image, (x, y), (x + w, y + h), color, 2)

        label = str(match) if match is not None else "?"
        cv2.putText(output_image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        if match is not None:
            elements.append((match, x))

    elements.sort(key=lambda x: x[1])

    for elem, _ in elements:
        expression.append(elem)

    cv2.imshow("Result", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if expression:
        expr = ''.join(expression)
        print(f"Detected expression: {expr}")
        try:
            result = eval(expr)
            print(f"Result of operation {expr} is: {result}")
        except Exception as e:
            print(f"Error in calculation: {e}")

numbers_path = 'dataset\\Numbers'
signes_path = 'dataset\\signes'
image_path = 'path_label\\screen4.jpg'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

process_image(binary_image, numbers_path, signes_path)
