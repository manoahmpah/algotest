import doctest


def test_ADN(liste = [""]):
    """
Documentation :
    Rôle : vérifie si la liste passée en paramètre
           ne contient que les quatre bases A, C, G et T comme valeurs

    Entré : une liste 
    Sortie : soit une erreur --> Pourquoi ? / booléen : False
             soit tous est bon ---> booléen : True

Exemple :
    >>> print(test_ADN(["G", "T", "A", "A"]))
    True
    >>> print(test_ADN(["G", "H", "A", "A"]))
    une lettre autre que A, G, C et T à été détecté dans la liste
    False
    >>> print(test_ADN(["G", 1, "A", "A"]))
    un nombre à été déctecté dans la liste
    False
    >>> print(test_ADN(["G", 1, "Q", "A"]))
    un nombre à été déctecté dans la liste
    False
    >>> print(test_ADN(["G", "Q", 1, "A"]))
    une lettre autre que A, G, C et T à été détecté dans la liste
    False
    >>> print(test_ADN([""]))
    True
    >>> print(test_ADN())
    True
    >>> print(test_ADN(['A', 'T', 'T', 'A', 'T', 'A', 'A', 'G', 'C', 'T', 'C', 'T', 'G', 'C', 'C', 'C', 'G', 'T', 'A', 'A', 'G', 'C', 'T', 'A', 'C', 'A', 'T', 'T', 'T', 'G', 'A', 'A', 'T', 'G', 'G', 'C', 'A', 'G', 'G', 'A', 'C', 'T', 'C', 'G', 'G', 'C', 'A', 'G', 'C', 'G', 'C', 'C', 'A', 'G', 'C', 'T', 'A', 'A', 'G', 'T', 'T', 'G', 'A', 'G', 'A', 'A', 'T', 'T', 'T', 'T', 'C', 'C', 'G', 'A', 'G', 'A', 'T', 'T', 'G', 'A', 'C', 'A', 'C', 'G', 'G', 'C', 'C', 'G', 'G', 'T', 'A', 'A', 'G', 'T', 'C', 'C', 'T', 'C', 'T', 'G']))
    True
    """
    i = 0
    nombre = 0
    while i != len(liste):
        if liste[i] == "A" or liste[i] == "G" or liste[i] == "T" or liste[i] == "C":
            i = i+1
        elif liste == [""]:
            return True 
        else:
            if type(liste[i]) == int or type(liste[i]) == float:
                print ("un nombre à été déctecté dans la liste")
                return False
            else:
                print("une lettre autre que A, G, C et T à été détecté dans la liste")
                return False

    return True
doctest.testmod(verbose=True)
help(test_ADN)
