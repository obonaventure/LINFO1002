

.. spelling::

   pylint
   autopep
   Ecrivez
   feedback
   framework
   frameworks
   l'implémentation
   illustratifs
   implémentation
   précondition
   préconditions
   formater
   wiki
   L'implémentation
   
   
Comment tester des fonctions en python ?
----------------------------------------

En parallèle avec l'apprentissage de l'écriture de programmes, un étudiant
en informatique doit aussi apprendre à écrire des tests qui permettent
de valider le bon fonctionnement des fonctions et programmes qu'il écrit.
Ces tests sont extrêmement importants pour avoir confiance dans la correction
d'un programme. Un programme est souvent composé d'un très grand nombre
de fonctions qui interagissent entre elles. La moindre erreur dans une de ces
fonctions peut avoir des conséquences catastrophiques sur le bon
fonctionnement du programme.

Il existe de nombreuses stratégies pour tester des programmes de façon
exhaustive. Dans le cadre de ce projet, nous n'entrerons pas dans tous ces détails, l'objectif est de faire une première sensibilisation à l'importance des
tests et d'encourager les étudiants à écrire des tests qui accompagnent
leurs programmes.

Souvent, les programmeurs débutants écrivent leurs tests en exécutant
manuellement leurs fonctions avec quelques valeurs d'entrée et observant
qu'elles fonctionnent correctement. D'autres ajoutent des appels à ``print``
dans leur code à certains endroits. Ces approches peuvent aider à détecter des
problèmes simples, mais elles sont à éviter en pratique. Leur inconvénient
majeur est qu'elles forcent le programmeur à passer beaucoup de temps pour
tester son programme. Comme celui-ci ou celle-ci manque souvent de temps, les
tests sont rarement exécutés et le code risque fort de ne pas être correct.

Une meilleure approche est de s'appuyer sur un framework de test qui permet
d'automatiser les tests. En utilisant un de ces frameworks, il suffit
de taper une commande pour vérifier que l'ensemble des tests du programme
continuent à s'exécuter correctement. L'apprentissage d'un tel framework
de test prend un peu de temps, mais il offre l'avantage de pouvoir facilement éviter les régressions. Une régression est une modification mineure du code qui
provoque une erreur subtile qui n'est pas détectée avant que le programme
ne soit finalisé. Avant cette correction, le programme fonctionnait
parfaitement et il suffit d'avoir changé quelques lignes pour qu'il se plante
lamentablement. 

Il existe plusieurs frameworks de test en python. Les plus connus sont `unittest <https://docs.python.org/3.5/library/unittest.html>`_, et `pytest <https://docs.pytest.org/en/latest/>`_ . Le wiki de Python contient une longue liste d'outils de test: https://wiki.python.org/moin/PythonTestingToolsTaxonomy

Dans la cadre de ce cours, nous nous concentrerons sur unittest, vous aurez
l'occasion d'apprendre d'autres frameworks de test dans le cadre d'autres cours d'informatique dans les prochaines années. Unittest est décrit en détails dans la documentation python : https://docs.python.org/3.5/library/unittest.html

Dans un premier temps, nous utiliserons unittest de façon à vérifier que l'implémentation d'une fonction écrite en python est correcte. Dans un second temps, nous utiliserons les tests à des fins pédagogiques et écrirons de petits exercices INGInious qui utilisent des tests unitaires écrits en utilisant unittest pour donner un feedback à des étudiants en informatique comme vous.

Tests unitaires simples
+++++++++++++++++++++++


Nos premiers tests unitaires avec unittest ont pour objectif de vérifier qu'une fonction correspondant à une spécification donnée fourni le résultat attendu. Commençons par quelques fonctions mathématiques simples. Notre premier exemple est le calcul de la valeur absolue. Même si python inclus la fonction ``abs()``, nous pouvons redéfinir une fonction équivalente nous-mêmes dans l'exemple ci-dessous.

.. literalinclude:: python/abs.py 
   :language: python 
   :linenos:

L'implémentation de la fonction ``my_abs()`` ne nécessite pas de commentaire
particulier. Par contre, nous pouvons regarder comment cette fonction est testée en utilisant unittest. Tout d'abord (première ligne du script), il faut importer le module unittest de façon à pouvoir utiliser ses fonctionnalités.

Avec unittest, un test unitaire s'écrit en étendant la classe ``unittest.TestCase`` et en ajoutant les méthodes permettant de tester les nouvelles fonctions. Dans le cas du calcul de la valeur absolue, nous avons ajouté la fonction ``test_my_abs()``. Celle-ci vérifie que la fonction ``my_abs()`` retourne le résultat attendu pour trois valeurs différentes de son argument:

 - ``my_abs(0)`` retourne ``0``
 - ``my_abs(1)`` retourne ``1``
 - ``my_abs(-1)`` retourne ``1``

Avec unittest, cette vérification se fait en utilisant un ensemble d'assertions. unittest définit dans la classe ``TestCase`` les assertions suivantes:    
      
 - ``assertEqual(a, b)`` vérifie que ``a == b``
 - ``assertNotEqual(a, b)`` vérifie que ``a != b``	 
 - ``assertTrue(x)`` vérifie que le booléen ``x`` s'évalue à ``True``
 - ``assertFalse(x)`` vérifie que le booléen ``x`` s'évalue à ``False``  
 - ``assertIs(a, b)`` vérifie que la référence ``a`` est le même objet que la référence ``b``
 - ``assertIsNot(a, b)`` vérifie que la référence ``a`` n'est pas le même objet que la référence ``b``
 - ``assertIsNone(x)`` vérifie que la référence ``x`` est ``None``
 - ``assertIsNotNone(x)`` vérifie que la référence ``x`` n'est pas ``None``
 - ``assertIn(a, b)`` vérifie que ``a`` est présent dans la liste ``b``
 - ``assertNotIn(a, b)`` vérifie que ``a`` n'est pas présent dans la liste ``b``
 - ``assertIsInstance(a, b)`` vérifie que ``a`` est une instance de la classe ``b``	
 - ``assertNotIsInstance(a, b)`` vérifie que ``a`` n'est pas une instance de la classe ``b``	


Ces méthodes vérifient leurs arguments en provoquent une erreur qui est reportée par unittest si une des assertions est invalidées.  Pour comprendre leur utilisation, revenons à notre exemple. Grâce au framework unittest, il est facile d'exécuter les tests en ligne de commande:

.. code-block:: console

   #python -m unittest -v abs
   test_my_abs (abs.TestAbs) ... ok

   ----------------------------------------------------------------------
   Ran 1 test in 0.002s

   OK

La suite de test a exécuté les trois tests définis ci-dessous. Modifions
maintenant l'implémentation de la fonction ``my_abs()``.

.. literalinclude:: python/abs2.py 
   :language: python 
   :linenos:

L'exécution de la suite de tests nous indique directement la régression et le message d'erreur nous montre l'assertion qui a échoué. Il ne nous reste plus qu'à corriger le code.

.. code-block:: console
                
   #python -m unittest -v abs2
   test_my_abs (abs2.TestAbs) ... FAIL

   ======================================================================
   FAIL: test_my_abs (abs2.TestAbs)
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "abs2.py", line 29, in test_my_abs
       self.assertEqual(my_abs(-1), 1)
   AssertionError: -1 != 1
   
   ----------------------------------------------------------------------
   Ran 1 test in 0.002s
   
   FAILED (failures=1)


                
La fonction valeur absolue est un fonction très simple à écrire et à tester.
D'autres fonctions sont plus compliquées. Prenons l'exemple classique du calcul de la médiane entre trois nombres ``a``,  ``b`` et ``c``. Vous avez proposé une solution pour calculer cette médiane au début de votre apprentissage de la programmation.

Voici quelques exemples de solutions proposées par les étudiants.

.. code-block:: python
		
   # Solution 1
   if (a<= c and c<=b) or (b<=c and c<=a):
       median = c
   elif (b<=a and a<=c) or (c<=a and a<=b):
       median = a
   else:
       median = b
   return median


.. code-block:: python

   # Solution 2
   if a>=b and a<=c:
       median=a
   elif b>=a and b<=c:
       median=c
   elif c>=a and c<=b:
        median=c
   return median

.. code-block:: python

   # Solution 3		
   median = a
   if a < b < c and c < b < a :
        median = b
   if b < c < a and a < c < b :
        median = c
   return median


Seule la première est correcte, les autres sont erronées. Même si le calcul de la médiane est un calcul simple, on peut rapidement se tromper dans l'imbrication des différents tests ou dans les conditions logiques et ces erreurs ne sont ni faciles à détecter ni à corriger. Pour tester qu'une telle fonction est correcte, différentes approches sont possibles.

Lorsque l'on demande à un programmeur débutant de tester sa solution, il fait en général quelques essais rapides et se convainc rapidement du bon fonctionnement de sa solution. Prenons quelques exemples illustratifs en supposant que la fonction est ``mediane(a,b,c)``. Pouvez-vous déterminer laquelle des assertions suivantes va permettre de détecter une erreur dans les solutions 2 et 3 ?

 - ``self.assertEqual(mediane(2,2,2), 2)``
 - ``self.assertEqual(mediane(1,2,3), 2)``
 - ``self.assertEqual(mediane(6,4,5), 5)``
 - ``self.assertEqual(mediane(8,-3,11), 8)`` 

Ces quatre assertions sont-elles suffisantes pour avoir la garantie que la fonction ``mediane(a,b,c)`` fonctionne correctement ?

Malheureusement non. Pour s'en rendre compte, considérons une implémentation un peu longue de la fonction ``mediane``.

.. code-block:: python
		
   def mediane(a,b,c):
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


Lorsque l'on exécute les quatre tests définis ci-dessus sur cette version de la fonction ``mediane``, quelles sont les parties du code qui sont vraiment exécutées ? Pour répondre à cette question, il faudrait exécuter pas à pas le programme et voir quelles branches il exécute. Manuellement ce serait fastidieux. Heureusement, il existe des programmes qui vous permettent de vérifier quelles sont les lignes qui sont exécutées. `Coverage.py <https://coverage.readthedocs.io/en/coverage-5.0.3/>`_ est un de ces outils. Il s'installe comme tout module python et interagit directement avec les tests unitaires unittest. Il mesure quelles lignes sont exécutées durant un test unitaire et présente un rapport en format HTML qui indique clairement la partie du code qui est testée par les tests et celle qui ne l'est pas. Si une partie de votre code n'est pas exécutée durant vos tests, c'est probablement une indication que ceux-ci ne sont pas suffisamment exhaustifs.

.. code-block:: console

   # coverage run -m unittest mediane3
   .
   ----------------------------------------------------------------------
   Ran 1 test in 0.000s
   
   OK
   # coverage html
   # browser htmlcov/index.html 


``Coverage.py`` s'exécute en ligne de commande. La figure ci-dessous montre le résultat obtenu avec le fichier :download:`python/mediane3.py`

.. figure:: /figures/coverage-mediane3.png

	  

Malheureusement, la réponse est non. Dans le cas du calcul de la médiane, la bonne façon de tester correctement le bon fonctionnement de cette fonction est testée toutes les combinaisons possibles des valeurs des variables ``a``, ``b`` et ``c``. Comme le résultat dépend uniquement des relations d'ordre entre les différentes valeurs des variables entières, il faut écrire des assertions dans lesquelles les valeurs des variables sont telles que :

 - ``a < b < c``
 - ``a < c < b``
 - ``b < a < c``
 - ``b < c < a``
 - ``c < a < b``
 - ``c < b < a``
   
Avec ces six tests, on couvre toutes les combinaisons d'arguments possibles. Ecrivez un test unitaire qui permet de valider l'implémentation correcte du calcul de la médiane.


Cette approche exhaustive dans laquelle on essaye toutes les combinaisons de valeurs possibles est intéressante car elle permet d'avoir confiance dans la correction de l'implémentation, mais il n'est pas toujours facile de définir les tests à réaliser. Il existe des théories qui permettent de produire les tests à réaliser pour vérifier une fonction dont on connaît la spécification, mais celle-ci sortent largement des objectifs d'un projet de première année. En outre, le nombre de tests à réaliser peut rapidement devenir très grand et il est en pratique difficile de les écrire. Pour s'en convaincre, il suffit de réfléchir à la façon dont on peut tester la fonction qui prend comme argument un tableau contenant un nombre impair d'entiers et retourne son élément médian.

.. code-block:: python

   def mediane(tab):
   """
   @pre: tab est un tableau contenant un nombre impair d'entiers
   @ post: retourne l'element median de ce tableau
   """		

Il n'est plus possible de tester cette fonction de façon exhaustive. Une approche raisonnable est de générer des tableaux contenant des nombres aléatoires et de vérifier que la fonction retourne le bon résultat dans tous les cas. 

.. literalinclude:: python/mediantab.py 
   :language: python 
   :linenos:


Ces tests unitaires sont l'occasion de montrer que les assertions de la classe ``unittest.TestCase`` prennent un troisième argument très utile en pratique: une chaîne de caractères à afficher lorsqu'une assertion n'est pas vérifiée. Ces messages d'erreur sont très utiles pour corriger les erreurs lorsque celles-ci sont détectées.
      
Prenons un autre exemple aussi extrait des exercices du premier cours d'informatique, le calcul du plus grand diviseur d'un entier positif. Cet exercice était proposé comme suit:

.. code-block:: console

   The Greatest Divisor of a number a is the biggest number ( except a itself) such that the division of a by this natural is an entire division.

   Since 0 is divisible by any natural this may cause some problems if you will look for the bigger one, so we expect you to return None.

   1 shall also return None.

   Recall that the operator % returns the remainder of the Euclidian division.


Cette question est intéressante car elle combine un calcul est des cas limites. Si l'argument est ``0`` ou ``1``, la fonction doit retourner ``None``. Sinon, elle doit retourner le plus grand diviseur. Voici quelques exemples de codes (pas nécessairement corrects) proposés par des étudiants sur INGInious et quelques tests unitaires.

.. literalinclude:: python/pgd.py 
   :language: python 
   :linenos:


Les assertions supportées par la classe ``unittest.TestCase`` permettent de couvrir la plupart des besoins. Il en existe d'autres que celles qui ont été présentées précédemment, dont:

 - ``assertAlmostEqual(a, b)`` qui permet de vérifier si le réel ``a`` est "proche" du réel ``b``. Lorsqu'un fonction réalise un calcul mathématique, celui-ci peut être entaché d'erreurs qui dépendent de la façon dont le calcul a été écrit. Le cours de méthodes numériques décrit des techniques qui permettent de minimiser ces pertes de précision, mais il est impossible de les éviter. Si une de vos fonctions retourne un réel, préférez ``assertAlmostEqual(a, b)`` à ``assertEqual(a, b)``. Vous pouvez utiliser les arguments optionnels ``place`` ou ``delta`` pour spécifier le niveau de précision que vous souhaitez.
 - ``assertNotAlmostEqual(a, b)``
 - ``assertGreater(a, b)``
 - ``assertGreaterEqual(a, b)``
 - ``assertLess(a, b)``
 - ``assertLessEqual(a, b)``


Il est aussi possible de définir des tests personnalisés en réutilisant ``assertTrue`` avec une expression booléenne bien choisie. Par exemple, si on veut vérifier que le résultat de la fonction ``f`` appliquée à ``7`` est pair, il suffit d'écrire ``assertTrue(f(7)%2==0)``. Lorsqu'une assertion existe dans ``unittest.TestCase``, il est préférable de l'utiliser cas cela rend les tests plus faciles à lire.
      
Quelques règles de bonne pratique
---------------------------------

L'écriture d'un ensemble pertinent de tests unitaires pour une fonction donnée s'apprend par la pratique. Il est difficile de lister des règles précises à suivre, mais voici quelques règles de bonne pratique qui peuvent s'avérer utile.

Considérons tout d'abord des fonctions qui n'ont pas d'effet de bord, c'est-à-dire des fonctions qui se contentent de lire leurs arguments (sans modifier leurs valeurs) et retournent un résultat. Pour ces fonctions, il est important de bien analyser les préconditions et de prendre en compte les cas suivants:

 - si la fonction prend des arguments entiers, tester avec ``0`` ainsi que des entiers positifs et négatifs qui respectent les préconditions
 - si la fonction prend une chaîne de caractères comme argument, voir comment elle réagit avec un chaîne vide, une chaîne contenant des caractères quelconques, une chaîne contenant des mots séparés par des espaces, virgules ou des retours à la ligne, voir si les chiffres ou caractères spéciaux sont bien supportés, voir s'il est possible de traiter une très longue chaîne de caractères, ...
 - si la fonction prend comme argument une liste, il est intéressant de tester une liste vide, une liste avec un seul élément, un liste contenant des éléments tous différents, une liste contenant plusieurs fois le même élément, ... Si le traitement fait dans la fonction dépend de l'ordre dans lequel les éléments sont placés dans la liste, ``random.shuffle()`` peut s'avérer très utile pour produire des variations d'un même liste dans un ordre différent. Si la fonction doit traiter des éléments se trouvant dans une liste, pensez à placer ces éléments au début, au milieu ou à la fin de la liste pour vérifier que la fonction traite bien tous les cas possibles.
 - si la fonction traite des fichiers, il faut penser à utiliser des fichiers vides, valides et invalides. Dans ce cas, on préférera généralement créer tous les fichiers au début de la suite de test en utilisant la méthode ``setUp`` et on veillera à les supprimer dans la méthode ``tearDown``  
   
      

Outils d'aide à l'écriture de programmes lisibles
-------------------------------------------------

Lorsque l'on écrit des programmes ou des suites de test en groupe, il est
important d'adopter les mêmes conventions d'écriture de façon à faciliter
la lecture du code par les différents membres du groupe. Différentes
communautés de programmeurs open-source ont développé des règles de bonne
pratique pour l'écriture de programmes, l'utilisation de l'indentation, des
espaces, etc. La communauté python a codifié ces règles de façon très précise
dans des documents tels que `PEP 8 -- Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`_

Certains éditeurs de programme python respectent ces conventions par défaut
ou vous aident à le faire. En outre, différents outils open-source
peuvent vous aider à adopter des conventions de codage uniformes.

Un premier outil est `autopep8 <https://pypi.org/project/autopep8/>`_
Il permet de formater automatiquement un code python de façon à ce qu'il
respecte le plus possible les conventions standard de codage en python.

Un deuxième outil est `pylint <https://www.pylint.org/>`_
Il est capable d'analyser votre code python pour voir si vous respectez
les règles définies dans PEP8, mais il comprend également de nombreux tests
qui détectent des erreurs liées une mauvaise utilisation des variables, la présence de code qui n'est pas exécuté, ...



