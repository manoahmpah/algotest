import doctest
def adn_brin2(liste = [""]):

    """ 
Documentation :

    Rôle : prend en paramètre une liste modélisant une
               séquence du brin e brin d adn n°1 et qui renvoie une liste modélisant la séquence du
               brin n°2 associé au brin n°1.
        Entrée : une liste de séquence ADN
        Sortie : soit c'est bon --> "l'opposer" du brin saisie
                 soit un nombre (ou chiffre) --> envoie un "un nombre (ou chiffre) à été détecter dans la liste : veulliez composer une liste que avec des lettres" 
                 soit une lettre qui n'est pas A, C, T et G --> envoie un "une lettre autre que A, G, C et T à été détecté dans la liste"
                 soit la liste est vide --> envoie "liste vide "

Exemple :

    >>> print(adn_brin2(['C', 'G', 'C', 'C', 'G', 'A', 'A', 'T', 'T']))
    ['G', 'C', 'G', 'G', 'C', 'T', 'T', 'A', 'A']
    >>> print(adn_brin2([""]))
    la liste est vide
    >>> print(adn_brin2(['C', 'G', 'C', 1, 'G', 'A', 'A', 'T', 'T']))
    un nombre (ou chiffre) à été détecter dans la liste : veulliez composer une liste que avec des lettres
    >>> print(adn_brin2(['C', 'G', 'M', 1, 'G', 'A', 'A', 'T', 'T']))
    une lettre autre que A, G, C et T à été détecté dans la liste
    """
    i = 0
    while len(liste) != i:
        if liste[i] == "A":
            liste.pop(i)
            liste.insert(i, "T")
            i = i+1
        elif liste[i] == "T":
            liste.pop(i)
            liste.insert(i, "A")
            i = i+1
        elif liste[i] == "G":
            liste.pop(i)
            liste.insert(i, "C")
            i = i+1
        elif liste[i] == "C":
            liste.pop(i)
            liste.insert(i, "G")
            i = i+1
        else:
            if type(liste[i]) == int or type(liste[i]) == float:
                return "un nombre (ou chiffre) à été détecter dans la liste : veulliez composer une liste que avec des lettres"
            elif liste == [""]:
                return "la liste est vide"
            elif liste[i] != "A" or liste[i] != "C" or liste[i] != "G" or liste[i] != "T":
                return "une lettre autre que A, G, C et T à été détecté dans la liste"
    return liste

# doctest.testmod(verbose=True)
# help(adn_brin2)

print(adn_brin2(['T', 'A', 'G', 'C', 'T', 'G', 'T', 'C', 'C', 'G', 'G', 'A', 'G', 'C', 'C', 'G', 'C', 'C', 'A', 'A', 'T', 'C', 'T', 'C', 'C', 'T', 'G', 'A', 'A', 'A', 'T', 'T', 'C', 'C', 'G', 'G', 'A', 'C', 'T', 'A']))