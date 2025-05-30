def correspond(mot, mot_a_trous):
    for i in range(len(mot_a_trous)):
        if len(mot) != len(mot_a_trous):
            return False
        elif mot_a_trous[i] != '*':
            if mot[i] != mot_a_trous[i]:
                return False
    return True
print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print( correspond('STOP', 'S*'))
print(correspond('AUTO', '*UT*'))

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinataires = 1
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires += 1
    return nb_destinataires == len(plan)
print(est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'}))
print(est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'}))
print(est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'}))
print(est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'}))