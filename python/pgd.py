#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 Exemple de test unitaire pour le calcul du plus grand diviseur
 O. Bonaventure, 2020
"""
import unittest

def pgd(a):
    """
     Exemple de code étudiant
    """
    l = []
    if a == 0:
        return None
    for i in range(1, a):
        while i <= a-1:
            if a%i == 0:
                l.append(i)
        l.reverse()
        return l[0]

def pgd2(a):
    """
     Exemple de code étudiant
    """
    l = []
    for i in range(a+1):
        if a <= 2:
            return None
        elif i >= 1 and a%i == 0 and i < a:
            l.append(i)

    return max(l)

def pgd3(a):
    """
     Exemple de code étudiant
    """
    if a == 0 or a == 1:
        return None
    else:
        l = []
        i = 1
        while i < a:
            if a%i == 0:
                l.append(i)
            i += 1
            return l[a]

def pgd4(a):
    """
     Exemple de code étudiant
    """
    if a <= 1:
        return None
    for div in range(a-1, 1, -1):
        if a%div == 0:
            return div
    return 1

class TestPGD(unittest.TestCase):
    """
     Classe de test permettant de valider le bon fonctionnement de pgd
    """

    def test_pgd(self):
        """
        @pre: -
        @post: a verifie le fonctionnement correct de la fonction pgd
        """
        self.assertIsNone(pgd(0), "Votre fonction ne retourne pas None"+
                          " lorsque son argument vaut 0")
        self.assertIsNone(pgd(1), "Votre fonction ne retourne pas None"+
                          " lorsque son argument vaut 1")
        self.assertEqual(pgd(2), 1,
                         "Votre fonction retourne "+str(pgd(2))+
                         " et non 1 lorsque son argument est 2")
        self.assertEqual(pgd(100), 50,
                         "Votre fonction retourne "+str(pgd(100))+
                         " et non 50 lorsque son argument est 100")
        self.assertEqual(pgd(37), 1,
                         "Votre fonction retourne "+str(pgd(37))+
                         " et non 1 lorsque son argument est 37")
        self.assertEqual(pgd(65), 13,
                         "Votre fonction retourne "+str(pgd(65))+
                         " et non 13 lorsque son argument est 65")


if __name__ == '__main__':
    unittest.main()
