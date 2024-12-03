import os
import shutil

def move_screen(filename, folder_name):
    
    # Vérifier si le fichier existe
    if not os.path.exists(filename):
        print(f"Le fichier {filename} est introuvable.")
        return
    
    # Créer le dossier s'il n'existe pas
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Construire le chemin de destination
    destination = os.path.join(folder_name, filename)
    
    # Déplacer le fichier
    try:
        shutil.move(filename, destination)
    except Exception as e:
        print(f"Erreur lors du déplacement de l'image : {e}")

