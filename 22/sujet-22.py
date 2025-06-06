def recherche(x, tab):
  indice = -1
  for i, k in enumerate(tab):
    if k == x:
      indice = i
  if indice == -1:
    return None
  return indice

print(recherche(1, [2, 3, 4])) # renvoie None
print(recherche(1, [10, 12, 1, 56]))
print(recherche(1, [1, 0, 42, 7]))
print(recherche(1, [1, 50, 1]))
print(recherche(1, [8, 1, 10, 1, 7, 1, 8]))

class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = [ "192.168.0.0", "192.168.255.255" ]
        return self.adresse in reservees

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = self.liste_octets()
        if octets[3] == 254:
            return None
        octet_nouveau = octets[3] + 1
        return AdresseIP('192.168.0.' + str(octet_nouveau))

adresse1, adresse2, adresse3 = AdresseIP('192.168.0.1'), AdresseIP('192.168.0.2'), AdresseIP('192.168.0.0')
print(adresse1.liste_octets())
print(adresse1.est_reservee())
print(adresse3.est_reservee())
print(adresse2.adresse_suivante().adresse)
