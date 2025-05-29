from random import randint
tab = [1, 52, 6, -9, 12]
def tri_selection(tab):
    for i in range(len(tab)):
        mini = tab[i]
        indice = i
        for y in  range(i + 1, len(tab)):
            if tab[y] < mini:
                mini = tab[y]
                indice = y
        if indice != i:
            tab[i], tab[indice] = tab[indice], tab[i]
    return tab

print(tri_selection(tab))


def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur + 1)
    else:
        print ("Perdu ! Le nombre était ", nb_mystere)

plus_ou_moins()

