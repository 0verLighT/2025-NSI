arbre = (((None, 1, None), 2, (None, 3, None)),4,((None, 5, None), 6, (None, 7, None)))


def parcours_largeur(arbre):
    if arbre is None:
        return []

    file = [arbre]
    resultat = []

    while file:
        g, x, d = file.pop(0)
        resultat.append(x)

        if g is not None:
            file.append(g)
        if d is not None:
            file.append(d)

    return resultat


parcours_largeur(arbre)


def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1, n):
        if sommes_max[i - 1] + tab[i] > tab[i]:
            sommes_max[i] = sommes_max[i - 1] + tab[i]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = sommes_max[0]
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]:
            maximum = i

    return sommes_max[maximum]

print(somme_max([1, 2, 3, 4, 5]))
print(somme_max([1, 2, -3, 4, 5]))
print(somme_max([1, 2, -2, 4, 5]))
print(somme_max([1, -2, 3, 10, -4, 7, 2, -5]))
