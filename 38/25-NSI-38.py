def moyenne(tab):
    somme=0
    for i in range(len(tab)):
        somme+=tab[i]
    moyenne= somme/len(tab)
    return print(moyenne)
moyenne([1.0])
moyenne([1.0, 2.0, 4.0])

def binaire(a):
    if a == 0:
        return '0'
    bin_a = ''
    while a>0 :
        bin_a = str(a%2) + bin_a
        a = a//2
    return print(bin_a)
binaire(83)
binaire(6)
binaire(127)
print(binaire(0))
