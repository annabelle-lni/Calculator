import cv2
import os
import shutil 


from save import move_screen
folder_name = "path_label"


#introduction 
print("📰 Instructions : Appuyer sur 'ESPACE' pour un screen ou sur 'ESC' pour quitter.")
print("📰 Instructions : Il y a 4 steps pour le traitement d'images :")
print("     # screen\n     # nuance de gris \n     # inverser les couleurs\n     # contraste")


# Activer la caméra
camera = cv2.VideoCapture(0)


if not camera.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()


while True:
    # Lire l'image de la caméra
    ret, frame = camera.read()
    if not ret:
        print("Erreur : Impossible de lire la vidéo.")
        break

    # flux video
    cv2.imshow("Camera", frame)

    # Attendre une touche
    key = cv2.waitKey(1) & 0xFF


    if key == 32:  # ESPACE for the screen
        #screen
        cv2.imwrite("screen1.jpg", frame)
        move_screen("screen1.jpg", folder_name)

        # Conversion en nuances de gris
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("screen2.jpg", gray_frame)
        move_screen("screen2.jpg", folder_name)


        #adaptive tresholding
        adaptive_thresh = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        cv2.imwrite("screen3.jpg", adaptive_thresh)
        move_screen("screen3.jpg", folder_name)

        #filtre median
        image_filtered = cv2.medianBlur(adaptive_thresh, 9)
        cv2.imwrite("screen4.jpg", image_filtered)
        move_screen("screen4.jpg", folder_name)

        from addtextfile import addtext #add tex

        break

    elif key == 27 : #appuyer sur esc pour quitter 
        break

# Libérer les ressources 
camera.release()
cv2.destroyAllWindows()
