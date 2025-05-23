class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit
a = Noeud(1, Noeud(4, None, None),Noeud(0, None,Noeud(7, None, None)))
def hauteur(noeud):
    if noeud is None:
        return -1
    return 1 + max(hauteur(noeud.gauche), hauteur(noeud.droit))

def taille(noeud):
    if noeud is None:
        return 0
    return 1 + taille(noeud.gauche) + taille(noeud.droit)

print(hauteur(a))
print(taille(a))
print(hauteur(None))
print(taille(None))
print(hauteur(Noeud(1,None, None)))
print(taille(Noeud(1, None, None)))

def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i]
    tab_ins[indice] = element
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i - 1]
    return tab_ins



print(ajoute(1, 4, [7, 8, 9]))
print(ajoute(3, 4, [7, 8, 9]))
print(ajoute(0, 4, [7, 8, 9]))

