def gb_vers_entier(tab):
        res = 0
        n = len(tab)
        for i in range(n):
            if tab[i]:
                res += 2 ** (n - 1 - i)
        return res


print(gb_vers_entier([]))
print(gb_vers_entier([True]))
print(gb_vers_entier([True, False, True,False, False, True, True]))
print(gb_vers_entier([True, False, False, False,
False, False, True, False]))


def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        j = i
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j-1
        tab[j] = valeur_insertion
tab = [5, 2, 9, 1, 3]
tri_insertion(tab)
print(tab)
