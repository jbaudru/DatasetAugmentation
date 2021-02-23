# Increase Dataset

## Histoire
> *Ce programme a été crée pour augmenter le nombre d'images dans le jeu de données disponnible en cliquant sur ce lien : https://drive.google.com/drive/folders/0B3P9oO5A3RvSUW9qTG11Ul83TEE . Le but était d'améliorer les performances d'un réseau de neurones reconnaissant les différentes classes de déchets. Ce projet est basé sur celui réalisé par https://github.com/garythung/trashnet. Ce programme rajoute, avec une certaine proba **p**, aux images de initiales : Une rotation (**p**=**1**), du floue (**p**=**1/4**), du bruit (**p**=**1/2**), un effet de lumière (**p**=**1/2**) et de la poussière (**p**=**1/2**).*

## Installation 
* Commande : `pip3 install pillow`

## Exécution
* Commande : `python3 data_augmentation.py`

## Input 
* Le dossier accessible via ce lien : https://drive.google.com/open?id=0B3P9oO5A3RvSNWw5X0c5R1hJRnc

## Output
* Le dossier accessible via ce lien : https://drive.google.com/open?id=1LnEmcOURzf7Q80CdLYHVRTjlAHE3JpeB 

## Remarques
* Pensez à modifier les chemins d'accès aux dossiers dans le code si besoin.
* Les images *dust_4.jpg*, *noise_5.jpg* et *flare_2.jpg* doivent se trouver dans le même dossier que le fichier *.py*.
