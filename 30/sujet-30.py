def delta(liste):
    resultat = [liste[0]]
    for i in range(1, len(liste)):
        resultat.append(liste[i] - liste[i - 1])
    return resultat

print(delta([1000, 800, 802, 1000, 1003]))
print(delta([42]))
class Expr:
    """Classe implémentant un arbre d'expression."""

    def __init__(self, g, v, d):
        """un objet Expr possède 3 attributs :
        - gauche : la sous-expression gauche ;
        - valeur : la valeur de l'étiquette, opérateur ou nombre ;
        - droite : la sous-expression droite."""
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        """renvoie True si et seulement 
        si le noeud est une feuille"""
        return self.gauche is None and self.droite is None

    def infixe(self):
        """renvoie la représentation infixe de l'expression en
        chaine de caractères"""
        s = ''
        if self.gauche is not None:
            s = s + '(' + self.gauche.infixe()
        s = s + str(self.valeur)
        if self.droite is not None:
            s = s + self.droite.infixe() + ')'
        return s

a = Expr(Expr(None, 1, None), '+', Expr(None, 2, None))
print(a.infixe())
b = Expr(Expr(Expr(None, 1, None), '+', Expr(None, 2, None)),
'*', Expr(Expr(None, 3, None), '+', Expr(None, 4, None)))
print(b.infixe())
e = Expr(
Expr(Expr(None, 3, None), '*', Expr(Expr(None, 8, None),
'+', Expr(None, 7, None))),
'-', Expr(Expr(None, 2, None), '+', Expr(None, 1, None)))
print(e.infixe())

