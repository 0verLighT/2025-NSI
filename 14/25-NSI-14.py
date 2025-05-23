from random import randint


def lancer(nb):
    return [randint(1, 6) for i in range(nb)]

def pair_6(tab):
    s = 0
    for i in tab:
        if i ==6:
            s = s + 1
    if s >= 2:
        return True
    else:
        return False

print(lancer(5))
print(lancer(5))
pair = lancer(5)
print(pair)
print(pair_6(pair))

def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_lignes(image)):
            nouvelle_image[i][j] = 255- image[i][j]
    return nouvelle_image

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 255 sinon'''
    nouvelle_image = [[0] * nombre_colonnes(image)
                      for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_lignes(image)):
            if image[i][j] < seuil :
                nouvelle_image[i][j] = 0
            else:
                nouvelle_image[i][j] = 255
    return nouvelle_image


img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69],[197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
print(nombre_lignes(img))
print(nombre_colonnes(img))
print(negatif(img))
print(binaire(img,120))