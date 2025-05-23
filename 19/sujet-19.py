def recherche_min(tab):
  mini = tab[0]
  indice = 0
  for i, k in enumerate(tab):
    if mini > k:
      mini = k
      indice = i
  return indice

print(recherche_min([5]))
print(recherche_min([2, 4, 1]))
print(recherche_min([5, 3, 2, 2, 4]))
print(recherche_min([-1, -2, -3, -3]))


def separe(tab):
  '''Separe les 0 et les 1 dans le tableau tab'''
  gauche = 0
  droite = len(tab) - 1
  while gauche < droite:
    if tab[gauche] == 0:
      gauche = gauche + 1
    else:
      tab[gauche] = tab[droite]
      tab[droite] = 1
      droite = droite - 1
  return tab

print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
print(separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]))
