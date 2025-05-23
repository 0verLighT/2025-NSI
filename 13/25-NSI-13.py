def recherche(x, tab):
  for i, p in enumerate(tab):
    if p == x:
      return i
  return None

print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))

def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a
                        # suivi des éléments de tab
    i = 0
    while i < ... and a > ...:
        tab_a[i] = ...
        tab_a[i+1] = a
        i = ...
    return tab_a

print(insere([1, 2, 4, 5], 3))
print(insere([1, 2, 7, 12, 14, 25], 30))
print(insere([2, 3, 4], 1))
print(insere([], 1))
