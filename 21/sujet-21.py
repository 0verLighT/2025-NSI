def indices_maxi(tab):
  maxi = tab[0]
  indice = [0]
  for i, k in enumerate(tab[1:], start=1):
    if k > maxi:
      maxi = k
      indice = [i]
    elif k == maxi:
      indice.append(i)
  return (maxi, indice)

print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))


def renverse(pile):
  '''renvoie une pile contenant les mêmes éléments que pile,
  mais dans l'ordre inverse.
  Cette fonction détruit pile.'''
  pile_inverse = []
  while pile != []:
    pile_inverse.append(pile.pop())
  return pile_inverse


def positifs(pile):
  '''renvoie une pile contenant les éléments positifs de pile,
  dans le même ordre. Cette fonction détruit pile.'''
  pile_positifs = []
  while pile != []:
    elem = pile.pop()
    if elem >= 0:
      pile_positifs.append(elem)
  return pile_positifs

print(renverse([1, 2, 3, 4, 5]))
print(positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print(positifs([-2]))
