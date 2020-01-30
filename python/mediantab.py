#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 Exemple de test unitaire pour le calcul de la mediane d'un tableau
 O. Bonaventure, 2020
"""
import unittest
import random

def mediane(tab):
    """
    @pre: t est un tableau contenant un nombre impair d'entiers
    @ post: retourne l'element median de ce tableau
    """
    if len(tab) > 1:
        milieu = int(len(tab)/2)
    else:
        milieu = 0
    stab = sorted(tab)
    return stab[milieu]

class TestMediane(unittest.TestCase):
    """
     Classe de test permettant de valider le bon fonctionnement de mediane
    """

    def test_mediane(self):
        """
        @pre: -
        @post: a verifie le fonctionnement correct de la fonction mediane
        """
        # Liste contenant un seul élément
        tab = [random.randint(3, 17)]
        self.assertEqual(mediane(tab), tab[0],
                         "Votre fonction appliquée à "+str(tab)+
                         " a retourné "+str(mediane(tab))+" et non "+
                         str(tab[0]))
        # Liste triée contenant trois éléments
        for _ in range(10):
            median = random.randint(3, 19)
            tab = [median-random.randint(1, 5), median,
                   median+random.randint(3, 9)]
            random.shuffle(tab)
            self.assertEqual(mediane(tab), median,
                             "Votre fonction appliquée à "+str(tab)+
                             " a retourné "+str(mediane(tab))+" et non "+
                             str(median))

        # Liste triée contenant cinq éléments
        for _ in range(10):
            tab = [None] * 5
            tab[0] = random.randint(3, 19)
            for j in range(1, 5):
                tab[j] = tab[j-1]+random.randint(3, 19)
            median = tab[2]
            random.shuffle(tab)
            self.assertEqual(mediane(tab), median,
                             "Votre fonction appliquée à "+str(tab)+
                             " a retourné "+str(mediane(tab))+" et non "+
                             str(median))



if __name__ == '__main__':
    unittest.main()
