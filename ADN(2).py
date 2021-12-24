import random
import doctest
def adn_brin1(n= '@'):
    """
Documentation :
    Rôle :  prend en paramètre un entier naturel n et qui
            renvoie une liste de taille n
    Entré : Entier naturel
    Sortie : liste renplie aléatoirement parmi
             les bases azotées "A","C","G" et "T".

Exemple :
        >>> print(adn_brin1(1.5))
        Erreur : choisi un chiffre ou nombre entier
        >>> print(adn_brin1("H"))
        Erreur : choisi un chiffre ou nombre entier
        >>> print(adn_brin1())
        Erreur : choisi un chiffre ou nombre entier


programme :
        vous dever copier : print(adn_brin1(#le chiffre de votre choix ... ))
        pour verfier que tous fonctionne car la liste est aléatoire
    """
    # Devensif 
    if type(n) == str or type(n) == float:
     return "Erreur : choisi un chiffre ou nombre entier"
    
    # le coeur du programme
    liste = [""]*n
    base = ["G", "A", "T", "C"]
    i = 0
    while len(liste) != i:
        liste.insert(i, random.choice(base))
        liste.pop()
        i = i + 1
    return liste


# doctest.testmod(verbose=True)
# help(adn_brin1)

print(adn_brin1())

