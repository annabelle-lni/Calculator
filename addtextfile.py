import cv2
import os

def addtext(folder_path, texts, output_prefix="screen_t"):

    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff'))]

    if len(image_files) != len(texts):
        print("Error: The number of images does not match the number of texts.")
        return

    for i, image_file in enumerate(image_files):
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Error: Unable to load {image_path}")
            continue

        text = texts[i]
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (0, 0, 255)
        thickness = 2

        text_x = 10
        text_y = image.shape[0] - 10

        cv2.putText(image, text, (text_x, text_y), font, font_scale, color, thickness)

        output_file = f"{output_prefix}{i + 1}.jpg"
        cv2.imwrite(output_file, image)
        print(f"🎀 Step {i+1} has been saved as: {output_file}")

    print("All images have been processed.")

#image_files = ["screen1.jpg", "screen2.jpg", "screen3.jpg", "screen4.jpg"]
folder_path = "path_label"
texts = ["Step 1: screenshot", 
         "Step 2: grayscale", 
         "Step 3: adaptive thresholding", 
         "Step 4: median filter"]

addtext(folder_path, texts)
