def min_et_max(tab):
  maxi = tab[0]
  mini = tab[0]
  for i in tab:
    if i >= maxi:
      maxi = i
    if i <= mini:
      mini = i
  return {"mini": mini, "maxi": maxi}
print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
print(min_et_max([0, 1, 2, 3]))
print(min_et_max([3]))
print(min_et_max([1, 3, 2, 1, 3]))
print(min_et_max([-1, -1, -1, -1, -1]))


class Carte:
  def __init__(self, c, v):
    """Initialise les attributs couleur (entre 1 et 4),
    et valeur (entre 1 et 13). """
    self.couleur = c
    self.valeur = v

  def recuperer_valeur(self):
    """ Renvoie la valeur de la carte :
    As, 2, ..., 10, Valet, Dame, Roi """
    valeurs = ['As', '2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'Valet', 'Dame', 'Roi']
    return valeurs[self.valeur - 1]

  def recuperer_couleur(self):
    """ Renvoie la couleur de la carte
    (parmi pique, coeur, carreau, trèfle). """
    couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
    return couleurs[self.couleur - 1]


class Paquet_de_cartes:
  def __init__(self):
    """Initialise l'attribut contenu avec une liste des 52 objets Carte,
    triés par valeurs croissantes, en commençant par pique, puis coeur, etc."""
    self.contenu = []
    for couleur in range(1, 5):  # 1 à 4 → pique à trèfle
      for valeur in range(1, 14):  # 1 à 13 → As à Roi
        self.contenu.append(Carte(couleur, valeur))


  def recuperer_carte(self, pos):
    """Renvoie la carte à la position pos (0 à 51)."""
    assert 0 <= pos < len(self.contenu), "paramètre pos invalide"
    return self.contenu[pos]

jeu = Paquet_de_cartes()
carte1 = jeu.recuperer_carte(20)
print(carte1.recuperer_valeur() + " de " + carte1.recuperer_couleur())
carte2 = jeu.recuperer_carte(0)
print(carte2.recuperer_valeur() + " de " + carte2.recuperer_couleur())
#carte3 = jeu.recuperer_carte(52) <- Erreur
