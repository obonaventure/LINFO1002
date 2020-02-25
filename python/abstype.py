"""
 Exemple de test unitaire pour le calcul de la valeur absolue
 O. Bonaventure, 2020
"""
import unittest
from typing import Union

def my_abs(i: int) -> int:
    """
    @pre: i est un entier
    @ post: retourne la valeur absolue de l'entier i
    """
    if i <= 0:
        return -i
    return i


def abs2(i: Union[int,float] ) -> Union[int,float]:
    """
    @pre: i est un nombre
    @ post: retourne la valeur absolue de l'entier i
    """
    if i <= 0:
        return -i
    return i

def print_abs(i: int) -> None:
    """
    @pre: i est un entier
    @ post: affiche la valeur absolue de l'entier i
    """
    if i <= 0:
        print (-i)
    print (i)





if __name__ == '__main__':
    print ( abs2 (-2) )
    print ( abs2 (-2.3) )

    print ( my_abs(2) )
    print ( my_abs(-2.5) )
    print ( my_abs( [-2] ) )
    print ( my_abs( "-2" ) )
    
    
