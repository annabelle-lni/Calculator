import cv2

def addtext(image_files, texts, output_prefix="screen_text"):

    if len(image_files) != len(texts):
        print("Erreur : le nombre d'images ne correspond pas au nombre de .")
        return

    for i, image_file in enumerate(image_files):
        image = cv2.imread(image_file)
        if image is None:
            print(f"Erreur : Impossible de charger {image_file}")
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
        print(f"🎀 Step {i+1} est sauvegardé sous: {output_file}")


    print("Toutes les images ont été traitées.")

image_files = ["screen1.jpg", "screen2.jpg", "screen3.jpg", "screen4.jpg"]
texts = ["Step 1 : screen", 
         "Step 2 : nuance de gris", 
         "Step 3 : couleurs inversées", 
         "Step 4 : contraste"]
addtext(image_files, texts)

