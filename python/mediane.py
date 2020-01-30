"""
 Tests unitaires pour le calcul de la médiane entre trois nombres
"""

import unittest


def mediane(a,b,c):
    """
    @pre: a, b, c entiers
    @post: retourne la médiane entre a, b et c
    """
    if a <= b and b <= c:
        return b

    if a <= c and c <= b:
        return c
    
    if b <= a and a <= c:
        return a

    if b <= c and c <= a:
        return c
    
    if c <= b and b <= a:
        return b
    
    if c <= a and a <= b:
        return a


class TestAbs(unittest.TestCase):
    """
    Tests unitaires pour le calcul de la mediane
    """

    def test_median(self):
        ''' Method with the test functions '''        
        self.assertEqual(mediane(2,2,2), 2)
        self.assertEqual(mediane(1,2,3), 2)
        self.assertEqual(mediane(3,2,1), 2)
        self.assertEqual(mediane(2,3,1), 2)
        self.assertEqual(mediane(1,3,2), 2)
        self.assertEqual(mediane(2,1,3), 2)
        self.assertEqual(mediane(3,1,2), 2)
        
if __name__ == '__main__':
    unittest.main()
