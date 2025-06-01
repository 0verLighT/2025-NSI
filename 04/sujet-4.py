def ecriture_binaire_entier_positif(n):
    res = ""
    if n == 0:
        return "0"
    while n > 0:
        res =  str(n % 2) + res
        n = n // 2
    return res

print(ecriture_binaire_entier_positif(0))
print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    tab[i], tab[j] = tab[j], tab[i]

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if tab[j] > tab[j+1]:
                echange(tab, j + 1, j)
    return tab

print(tri_bulles([]))
print(tri_bulles([9, 3, 7, 2, 3, 1, 6]))
print(tri_bulles([9, 7, 4, 3]))
