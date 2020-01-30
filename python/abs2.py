"""
 Exemple de test unitaire pour le calcul de la valeur absolue, avec
 une implementation en erreur
 O. Bonaventure, 2020
"""
import unittest

def my_abs(i):
    """
    @pre: i est un entier
    @ post: retourne la valeur absolue de l'entier a
    """
    if i <= 0:
        return i
    return i

class TestAbs(unittest.TestCase):
    """
     Classe de test permettant de valider le bon fonctionnement de my_abs
    """

    def test_my_abs(self):
        """
        @pre: -
        @post: a verifie le fonctionnement correct de la fonction my_abs
        """
        self.assertEqual(my_abs(1), 1)
        self.assertEqual(my_abs(0), 0)
        self.assertEqual(my_abs(-1), 1)


if __name__ == '__main__':
    unittest.main()
