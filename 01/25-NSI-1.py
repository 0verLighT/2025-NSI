def voisins_entrants(liste, i):
    '''Renvoie la liste des voisins de l'élément d'indice i dans liste.'''
    voisins = []
    if i > 0:
        voisins.append(liste[i - 1])
    if i < len(liste) - 1:
        voisins.append(liste[i + 1])
    return voisins

print(voisins_entrants([[1, 2], [2], [0], [0]], 0))
print(voisins_entrants([[1, 2], [2], [0], [0]], 1))


def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)):
        if s[i] == chiffre:
            compte += 1
        else:
            resultat += str(compte) + chiffre
            chiffre = s[i]
            compte = 1
    resultat += str(compte) + chiffre
    return resultat


print(nombre_suivant('1211'))
print(nombre_suivant('311'))

