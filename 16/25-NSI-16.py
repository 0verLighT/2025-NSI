def moyenne(tab):
    s = 0
    c = 0
    for item in tab:
        s = s + item[0] * item[1]
        c = c + item[1]
    return s / c
print(moyenne([(15.0,2),(9.0,1),(12.0,3)]))


def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1]
    for i in range(len(ligne)-1):
        ligne_suiv.append(ligne[i+1]  + ligne[i])
    ligne_suiv.append(1)
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(n):
        ligne_k =  ligne_suivante(triangle[-1])
        triangle.append(ligne_k)
    return triangle

print(ligne_suivante([1, 3, 3, 1]))
print(pascal(2))
print(pascal(3))

