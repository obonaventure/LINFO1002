#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 Exemple d'utilisation de l'analyse statique
 O. Bonaventure, 2020
"""
from typing import List, Dict

def presences(val, tab):
    """
    @pre: tab est un tableau 
          val une valeur d'un type quelconque
    @ post: retourne le nombre de fois que val est repris dans tab
    """
    count = 0
    for e in tab:
        if e==val:
            count += 1
    return count


def presences2(val : int, tab: List[int]) -> int :
    """
    @pre: tab est un tableau 
          val une valeur d'un type quelconque
    @ post: retourne le nombre de fois que val est repris dans tab
    """
    count = 0
    for e in tab:
        if e==val:
            count += 1
    return count
    
def present(n: int, tab: List[int]) -> bool:
    """
    @pre: tab est un tableau contenant des entiers
          n un entier
    @ post: retourne True si n est présent dans tab, False sinon
    """

    for e in tab:
        if e==n:
            return True
    return False


if __name__ == '__main__':
    print (presences(1, [2,3,4]) )
    print (presences('a', [2,3,4]) )    
    print (presences('a', [2,'a',4,'a','b']) )
    print (presences(['a'], [2,['a'],4,('a'),'b']) )    
