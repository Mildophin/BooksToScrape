## Fonctionnement
Le programme va analyser la page d'accueil du site et déterminer le nombre de pages totales puis
en fonction de celui-ci, analyser toutes les pages et récupérer le lien de chaque livre présent sur
Chaque page (50*20 livres dans ce cas-ci). Puis le programme va analyser la page de chaque livre
et en retirer les informations que l'on cherche (titre, description, note, etc..), mettre les infos dans
un dictionnaire en fonction de la catégorie et téléchargera la photo du livre dans un dossier photo.
Puis le programme va analyser tous les dictionnaires de catégories créés et va créer un fichier csv
pour chacune d'entre elles.


## Installation
Taper "pip install -r requirements.txt" pour installer les dépendances dans l'environnement virtuel
puis exécuter le fichier main.py (pour windows: py main.py, et pour unix: python3 main.py)






