
Analyse statique
================

Comme vous l'avez vu dans le premier cours de programmation consacré
au langage python, celui-ci est un langage non-typé. Lorsque vous
écrivez une fonction en python, et contrairement à d'autres
langages de programmation tels que Java, ou C que vous verrez l'année
prochaine, python ne vous oblige pas à préciser le le type des arguments
de la fonction et le type de résultat que celle-ci va retourner. Cette
flexibilité est pratique dans certains cas. Par exemple, supposons que vous
devez écrire une fonction qui permet de déterminer le nombre de fois qu'une
valeur est présent dans une liste.

En python3, cette fonction peut s'écrire comme suit.

.. code-block:: python

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


Elle peut s'utiliser avec n'importe que type de données comme illustré ci-dessous.

.. code-block:: python

    print (presences(1, [2,3,4]) )  # affiche 0
    print (presences('a', [2,3,4]) )  # affiche 0   
    print (presences('a', [2,'a',4,'a','b']) ) # affiche 2
    print (presences(['a'], [2,['a'],4,('a'),'b']) ) # affiche 1    


Certains considèrent que cette possibilité de supporter n'importe quel type de données comme étant un des avantages importants de python. D'autres et notamment ceux qui doivent gérer des codes de très grande taille sont parfois plus mitigés. La liberté offerte par python s'accompagne parfois de bugs difficiles à détecter et qui sont liés à une utilisation incorrecte de certains fonctions qui n'est détectée qu'à l'exécution et provoque des erreurs qui affectent les utilisateurs. La société Dropbox par exemple utilise plusieurs millions de ligne de code écrit en python. Elle a d'ailleurs engagé l'inventeur de python pendant plusieurs années. Dans un `blog publié fin 2009 <https://blogs.dropbox.com/tech/2019/09/our-journey-to-type-checking-4-million-lines-of-python/>`_, les informaticiens de Dropbox expliquent comment ils ont petit à petit converti leur code python de façon à forcer les développeur à indiquer clairement les types de données qu'ils utilisent. Cela réduit la liberté du développeur, mais permet d'éviter de très nombreux bugs. Cette approche est implémentée par l'utilitaire `mypy <https://mypy.readthedocs.io/en/stable/>`_ et supportée par les versions récentes de python. Elle s'appuie sur le typage statique, une technique utilisée par de nombreux langages de programmation et compilateurs.

Python3 support plusieurs types de données primitifs dont les entiers, les booléens, les réels, les chaînes de caractères, ... Chacun de ces types est identifié par un mot-clé spécifique.

 - ``int`` : nombre entier
 - ``float`` : nombre réel en virgule flottante
 - ``bool`` : booléen (``True`` ou ``False``)	
 - ``str`` : chaîne de caractères en représentation Unicode
 - ``bytes`` : chaîne de d'octets
 - ``object`` : objet python quelconque (classe mère de tous les objets)

Il est possible de combiner ces différents types de données primitifs dans des listes, tuples, dictionnaires, ...


 - ``List[str]`` : une liste contenant uniquement des chaînes de caractères
 - ``Tuple[int, float]`` : un tuple contenant un entier et un réel
 - ``Tuple[int, ...]`` : un tuple contenant un nombre quelconque d'entiers
 - ``Dict[str, float]`` : un dictionnaire qui fait correspondre une chaîne de caractères à un réel

D'autres structures de données sont définies dans la documentation de `mypy <https://mypy.readthedocs.io/en/stable/>`_ .

Grâce à ces identifiants de types de données, il est possible d'annoter les signatures des fonctions de façon à indiquer le type des arguments qu'elle reçoit et les types de résultats qu'elle retourne. Commençons par repartir de la fonction qui calcule la valeur absolue d'un entier. Avec le typage statique, celle-ci doit s'écrire:

.. code-block:: python

   def my_abs(i: int) -> int:
    """
    @pre: i est un entier
    @ post: retourne la valeur absolue de l'entier i
    """
    if i <= 0:
        return -i
    return i


Les modifications se retrouvent dans la signature de la fonction qui inclus maintenant le type de son argument et le type de son résultat. Pour comprendre l'intérêt du typage statique, considérons un étudiant qui essaie d'utiliser la fonction ``my_abs`` de la façon suivante :

.. code-block:: python

    print ( my_abs(2) )
    print ( my_abs(-2.5) )
    print ( my_abs( [-2] ) )
    print ( my_abs( "-2" ) )

Lorsque ces différentes lignes sont exécutées, l'interpréteur python affiche les messages suivants:

.. code-block:: python
                
   2
   2.5
   Traceback (most recent call last):
     File "python/abstype.py", line 32, in <module>
       print ( my_abs( [-2] ) )
     File "python/abstype.py", line 12, in my_abs
       if i <= 0:
     TypeError: '<=' not supported between instances of 'list' and 'int'

Les deux premières lignes sont correctes. Ensuite, python affiche des messages d'erreur car la fonction n'est pas prévue pour fonctionner avec une liste, un tuple ou une chaîne de caractères. Si de telles erreurs sont détectées lors de l'exécution du programme par l'utilisateur, c'est genant car en général celui-ci n'a aucune idée de l'origine de l'erreur et ne sait pas la corriger. Dans un exercice inginious, c'est aussi une source de nombreuses erreurs pour des étudiants. Le typage statique permet de valider les types des arguments et des valeurs de retour des fonctions. Dans l'exemple ci-dessous, ``mypy`` indique les erreurs suivantes:

.. code-block:: python

   python/abstype.py:2: error: Argument 1 to "my_abs" has incompatible type "float"; expected "int"
   python/abstype.py:3: error: Argument 1 to "my_abs" has incompatible type "List[int]"; expected "int"
   python/abstype.py:4: error: Argument 1 to "my_abs" has incompatible type "str"; expected "int"



Certains fonctions ne retournent pas de résultat. Dans ce cas, il faut indiquer dans leur signature qu'elles retournent ``None``. 
                

.. code-block:: python

   def print_abs(i: int) -> None:
    """
    @pre: i est un entier
    @ post: affiche la valeur absolue de l'entier i
    """
    if i <= 0:
        print (-i)
    print (i)


Il est aussi possible de spécifier des listes ou des dictionnaires comme arguments en indiquant les types primitifs que ces arguments contiennent.

.. code-block:: python

   def presences(val : int, tab: List[int]) -> int :
    """
    @pre: tab est une liste d'entiers 
          val un entier
    @ post: retourne le nombre de fois que val est repris dans tab
    """
    count = 0
    for e in tab:
        if e==val:
            count += 1
    return count



Dans certains cas, il est nécessaire d'écrire des fonctions qui peuvent supporter des arguments de plusieurs types différents. Dans le cas de notre exemple avec la valeur absolue, cette fonction est définie pour les entiers et les réels. Il est possible d'indiquer à ``mypy`` qu'une fonction peut recevoir un entier ou un réel via le mot clé ``Union``. Celui-ci s'utilise comme dans l'exemple ci-dessous.

.. code-block:: python

   def abs2(i: Union[int,float] ) -> Union[int,float]:
    """
    @pre: i est un nombre
    @ post: retourne la valeur absolue de l'entier i
    """
    if i <= 0:
        return -i
    return i


Cette fonction est validée par ``mypy`` et s'utilise avec des réels ou des entiers.

.. code-block:: python

    print ( abs2 (-2) )     # affiche 2
    print ( abs2 (-2.3) )   # affiche 2.3

    
 
Dans le cadre d'exercices inginious, le typage statique facilite l'écriture du code de test et permet d'être sûr que l'étudiant utilise bien les arguments du bon type. Cela évite de devoir vérifier manuellement que les préconditions (au niveau des types de données) sont bien respectées. Le manuel officiel de ``mypy`` disponible via 

    
