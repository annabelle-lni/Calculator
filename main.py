import cv2
import os
import sys



# Activer la caméra
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()

print("📰 Instructions : Appuyer sur 'ESPACE' pour un screen ou sur 'ESC' pour quitter.")
print("📰 Instructions : Il y a 4 steps pour le traitement d'images :")
print("     # screen\n     # nuance de gris \n     # inverser les couleurs\n     # contraste")



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
        cv2.imwrite("screen1.jpg", frame)

        # Conversion en nuances de gris
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("screen2.jpg", gray_frame)
    
        #inverser les couleurs
        img_inv = cv2.bitwise_not(gray_frame)
        cv2.imwrite("screen3.jpg", img_inv)

        #accentuer le contraste
        th, contraste = cv2.threshold(img_inv, 128, 192, cv2.THRESH_BINARY)
        cv2.imwrite("screen4.jpg", contraste)



        from addtextfile import addtext #add text
        break

    elif key == 27 : #appuyer sur esc pour quitter 
        break


# Libérer les ressources 
camera.release()
cv2.destroyAllWindows()
