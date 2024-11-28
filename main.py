import cv2

# Activer la caméra
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra.")
    exit()

print("📰 Instructions : Appuyer sur 'ESPACE' pour un screen ou sur 'q' pour quitter.")

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
        print("🎀 Step 1 : image normale : 'screen1.jpg'.")
        cv2.imwrite("screen1.jpg", frame)

        # Conversion en nuances de gris
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        print("🎀 Step 2 : nuance de gris : 'screen.jpg'.")
        cv2.imwrite("screen2.jpg", gray_frame)









        
        break
    elif key == 27 : #appuyer sur esc pour quitter 
        break


# Libérer les ressources 
camera.release()
cv2.destroyAllWindows()
