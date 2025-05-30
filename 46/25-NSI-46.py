def compte_occurrences(x,tab):
    l=0
    for i in range(len(tab)):
        if tab[i]==x:
            l+=1
    return l
print(compte_occurrences(5, []))
print(compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]))
print(compte_occurrences('a',  ['a','b','c','a','d','e','a']))
def rendu_monnaie(somme_due, somme_versee):

    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0:
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(pieces[i])
        a_rendre = a_rendre - pieces[i]
    return rendu
pieces = [1, 2, 5, 10, 20, 50, 100, 200]
print(rendu_monnaie(700, 700))
print(rendu_monnaie(102, 500))