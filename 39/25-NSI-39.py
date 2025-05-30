def moyenne(tab):
    somme=0
    if len(tab) == 0:
        return None
    for i in range(len(tab)):
        somme=somme+tab[i]
    moyenne= somme/len(tab)
    return moyenne
print(moyenne([5,3,8]))
print(moyenne([1,2,3,4,5,6,7,8,9,10]))
print(moyenne([]))


def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0
    j = len(tab) - 1

    while i < j:
        if tab[i] == 0:
            i += 1
        else:
            valeur = tab[i]
            tab[i] = tab[j]
            tab[j] = valeur
            j -= 1
tab = [0, 1, 0, 1, 0, 1, 0, 1, 0]
tri(tab)
print(tab)