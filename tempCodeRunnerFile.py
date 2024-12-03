import os
import cv2
import numpy as np

def load_templates(numbers_path, signes_path):
    templates = {}

    for i in range(10):
        template_path = os.path.join(numbers_path, f"num{i}.jpg")
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is not None:
            templates[i] = template
        else:
            print(f"Erreur : {template_path} introuvable ou non lisible.")

    operations = {"add": "+", "sub": "-", "mult": "*", "div": "/"}
    for key, symbol in operations.items():
        template_path = os.path.join(signes_path, f"{key}.jpg")
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is not None:
            templates[symbol] = template
        else:
            print(f"Erreur : {template_path} introuvable ou non lisible.")

    if not templates:
        print("Aucun modèle valide chargé.")
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

def process_image(image, numbers_path, signes_path):
    if len(image.shape) != 2 or np.max(image) > 255 or np.min(image) < 0:
        print("L'image n'est pas binaire.")
        return

    templates = load_templates(numbers_path, signes_path)
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

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

    cv2.imshow("Résultat", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

numbers_path = 'dataset\\Numbers'
signes_path = 'dataset\signes'
image_path = 'path_label\screen4.jpg'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

process_image(binary_image, numbers_path, signes_path)
