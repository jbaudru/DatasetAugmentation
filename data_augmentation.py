import os
import random
from PIL import Image, ImageFilter

INPUT_DIRECTORY = "dataset-resized/"
OUTPUT_DIRECTORY = "dataset-resized-augment/"

#=== Affiche instructions ======================================================
def instruction():
    print(" \n######################################################")
    print(" #                                                    #")
    print(" #      AUGMENTATION DU JEU DE DONNEES INITIAL        #")
    print(" #                                                    #")
    print(" ######################################################")
    print(" # Instructions :                                     #")
    print(" # ==============                                     #")
    print(" #   1 - Supprimez le fichier .DS_Store dans          #")
    print(" #       le dossier 'dataset-resized'.                #")
    print(" #   2 - Lancez le programme dans le dossier parent   #")
    print(" #       du dosser 'dataset-resized'.                 #")
    print(" #   3 - Le traitement des images peut prendre un     #")
    print(" #       moment si le dossier est volumineux.         #")
    print(" #                                                    #")
    print(" ######################################################")
    print(" # Résultat :                                         #")
    print(" # ==========                                         #")
    print(" #   1 - Un dossier 'data_folder_augment' avec des    #")
    print(" #       images uniformisées, bruitées et translatées.#")
    print(" #                                                    #")
    print(" #                                          J. BAUDRU #")
    print(" ######################################################\n")

#=== Vérifie les noms des dossiers sources et destination ======================
def main():
    instruction()
    data_folder = INPUT_DIRECTORY
    data_folder_augment = OUTPUT_DIRECTORY
    if(os.path.isdir(data_folder_augment)!= True):
        os.mkdir(data_folder_augment)
    if(os.path.isdir(data_folder)!= True):
        print( "[Erreur] - Vous n'avez pas fourni de dossier correct.")
        quit()
    else:
        list_type_folder = os.listdir(data_folder)
        list_photo_tt_type = []
        for i in range(0,len(list_type_folder) ):
            chemin = data_folder+list_type_folder[i]
            list_photo_type = os.listdir(chemin)
            for j in range(0,len(list_photo_type)):
                list_photo_type[j] = chemin + "/" + list_photo_type[j]
            list_photo_tt_type.append(list_photo_type)

        modify_image(list_photo_tt_type, data_folder, data_folder_augment)

#=== Transforme une image en quatre images différentes =========================
def modify_image(list_image,folder_src, folder_dest):
    area = (0, 0, 384, 384)
    size = (825, 825)
    angle1 = 90; angle2 = 180; angle3 = 270
    #NOTE : Gère la création des différents dossiers d'images
    tras_fold = folder_dest + "trash/"
    plat_fold = folder_dest + "plastic/"
    pape_fold = folder_dest + "paper/"
    meta_fold = folder_dest + "metal/"
    glas_fold = folder_dest + "glass/"
    card_fold = folder_dest + "cardboard/"
    if(os.path.isdir(plat_fold)!= True):
        os.makedirs(plat_fold)
    if(os.path.isdir(pape_fold)!= True):
        os.makedirs(pape_fold)
    if(os.path.isdir(meta_fold)!= True):
        os.makedirs(meta_fold)
    if(os.path.isdir(glas_fold)!= True):
        os.makedirs(glas_fold)
    if(os.path.isdir(card_fold)!= True):
        os.makedirs(card_fold)
    if(os.path.isdir(tras_fold)!= True):
        os.makedirs(tras_fold)

    print(' > Traitement en cours ...')
    for i in range(0,len(list_image)):
        for j in range(0,len(list_image[i])):
            #NOTE : Crée les quatres images et les envoie dans la fonction d'effet
            imageee = Image.open(list_image[i][j])
            imageee = rotate_crop_fx_image(imageee,0, area)
            imageee_rot1 = Image.open(list_image[i][j])
            imageee_rot1 = rotate_crop_fx_image(imageee_rot1, angle1, area)
            imageee_rot2 = Image.open(list_image[i][j])
            imageee_rot2 = rotate_crop_fx_image(imageee_rot2, angle2, area)
            imageee_rot3 = Image.open(list_image[i][j])
            imageee_rot3 = rotate_crop_fx_image(imageee_rot3, angle3, area)
            #NOTE : Gère le noms des différents dossiers d'images
            if(list_image[i][j][len(folder_src)::][:3] == "tra"):
                folder = tras_fold
            elif(list_image[i][j][len(folder_src)::][:3] == "pla"):
                folder = plat_fold
            elif(list_image[i][j][len(folder_src)::][:3] == "pap"):
                folder = pape_fold
            elif(list_image[i][j][len(folder_src)::][:3] == "met"):
                folder = meta_fold
            elif(list_image[i][j][len(folder_src)::][:3] == "gla"):
                folder = glas_fold
            elif(list_image[i][j][len(folder_src)::][:3] == "car"):
                folder = card_fold
            #NOTE : Gère le noms des quatres images crées
            nom1 = str(folder_dest) + str((list_image[i][j][len(folder_src)::])[:-4]) + "_0.jpg"
            nom2 = folder_dest + (list_image[i][j][len(folder_src)::])[:-4] + "_90.jpg"
            nom3 = folder_dest + (list_image[i][j][len(folder_src)::])[:-4] + "_180.jpg"
            nom4 = folder_dest + (list_image[i][j][len(folder_src)::])[:-4] + "_270.jpg"
            #NOTE : Enregistre les images crées
            imageee = imageee.save(nom1)
            imageee_rot1 = imageee_rot1.save(nom2)
            imageee_rot2 = imageee_rot2.save(nom3)
            imageee_rot3 = imageee_rot3.save(nom4)
    print(' > Traitement terminé.\n')

#=== Effet sur les images ======================================================
def rotate_crop_fx_image(image, angle, area):
    image = image.crop(area)
    image = image.rotate(angle)
    image = random_noise(image, angle)
    image = random_dust(image, angle)
    image = random_flare(image, angle)
    image = random_flou(image)
    return image

#=== Une chance sur trois que l'image soit poussièreuse ========================
def random_dust(imageee, angle):
    res = random.randint(0,2)
    size = 1000,1000
    area = (0, 0, 384, 384)
    if(res == 0):
        noise = Image.open('dust_4.jpg')
        noise = noise.resize(size, Image.ANTIALIAS)
        noise = noise.crop(area)
        noise = noise.rotate(-angle)
        imageee = Image.blend(imageee, noise, .3)
    return imageee

#=== Une chance sur trois que l'image soit bruitée =============================
def random_noise(imageee, angle):
    res = random.randint(0,2)
    size = 1000,1000
    area = (0, 0, 384, 384)
    if(res == 0):
        noise = Image.open('noise_5.jpg')
        noise = noise.resize(size, Image.ANTIALIAS)
        noise = noise.crop(area)
        noise = noise.rotate(-angle)
        imageee = Image.blend(imageee, noise, .180)
    return imageee

#=== Une chance sur trois que l'image soit poussièreuse ========================
def random_flare(imageee, angle):
    res = random.randint(0,2)
    size = 1000,1000
    area = (0, 0, 384, 384)
    if(res == 0):
        noise = Image.open('flare_2.jpg')
        noise = noise.resize(size, Image.ANTIALIAS)
        noise = noise.crop(area)
        noise = noise.rotate(-angle)
        imageee = Image.blend(imageee, noise, .3)
    return imageee

#=== Une chance sur trois que l'image soit floue ===============================
def random_flou(imageee):
    res = random.randint(0,4)
    if(res == 0):
        imageee = imageee.filter(ImageFilter.GaussianBlur(3))
    return imageee


if __name__ == '__main__':
    main()
