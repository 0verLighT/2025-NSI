def moyenne(notes):
    somme = 0
    somme_coeff = 0
    for i in range(len(notes)):
        somme = somme + (notes[i][0] * notes[i][1])
        somme_coeff += notes[i][1]
    if somme_coeff == 0:
        return None
    moyenne = somme / somme_coeff
    return moyenne

print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))

def affiche(dessin):
    '''Affichage d'une grille : les 1 sont représentés par un "*" , les 0 par une espace " "'''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage += "*"
            else:
                affichage += " "
        print(affichage)

def liste_zoom(liste_depart, k):
    '''Renvoie une liste contenant k fois chaque élément de liste_depart'''
    liste_zoomee = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoomee.append(elt)
    return liste_zoomee

def dessin_zoom(grille, k):
    '''Renvoie une grille où les lignes sont zoomées k fois ET répétées k fois'''
    grille_zoomee = []
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne, k)
        for i in range(k):
            grille_zoomee.append(ligne_zoomee)
    return grille_zoomee
coeur = [
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
]

print("Cœur original :")
affiche(coeur)

print("\nCœur zoomé x2 :")
affiche(dessin_zoom(coeur, 2))
print(liste_zoom([1, 2, 3], 3))