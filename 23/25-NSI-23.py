notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7,9, 9, 5, 0, 9, 6, 5, 4]


def effectif_notes(notes_eval):
  """Renvoie un tableau des effectifs des notes de 0 à 10."""
  effectifs = [0] * 11
  for note in notes_eval:
    effectifs[note] += 1
  return effectifs

def notes_triees(effectifs):
    """Renvoie une liste de notes triées à partir du tableau des effectifs."""
    notes = []
    for note, nb_occurrences in enumerate(effectifs):
      notes.extend([note] * nb_occurrences)
    return notes

print(notes_triees(effectif_notes(notes_eval)))
print(effectif_notes(notes_eval))

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)


def bin_to_dec(nb_bin):
  if len(nb_bin) == 1:
    if nb_bin == '0':
      return 0
    else:
      return 1
  else:
    if nb_bin[-1] == '0':
      bit_droit = 0
    else:
      bit_droit = 1
    return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit


print(dec_to_bin(25))
print(bin_to_dec('101010'))
