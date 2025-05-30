def ou_exclusif(a,b):
    c=[]
    for i in range(len(a)):
        if a[i] == b[i]:
            c.append(0)
        else:
            c.append(1)
    return print(c)
ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0])
ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1])

class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

    def affiche(self):
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        return sum(self.tableau[i])

    def somme_col(self, j):
        return sum(self.tableau[i][j] for i in range(self.ordre))

    def est_semimagique(self):
        s = self.somme_ligne(0)

        # Vérifie les lignes
        for i in range(1, self.ordre):
            if self.somme_ligne(i) != s:
                return False

        # Vérifie les colonnes
        for j in range(self.ordre):
            if self.somme_col(j) != s:
                return False

        return True
lst_c3 = [3, 4, 5, 4, 4, 4, 5, 4, 3]
c3 = Carre(lst_c3, 3)
c3.affiche()