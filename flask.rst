.. LINFO1002 documentation master file, created by
   sphinx-quickstart on Tue Jan 28 18:06:33 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Le framework flask
==================

Il existe de nombreuses librairies qui permettent de faciliter l'écriture de
sites web interactifs en Python: `Django <https://www.djangoproject.com/>`_,
`Webpy <https://webpy.org/>`_ ou `flask <https://palletsprojects.com/p/flask/>`_. Dans le cadre de ce projet
nous avons choisi `flask <https://palletsprojects.com/p/flask/>`_ qui a l'avantage d'être simple à apprendre tout en pouvant profiter de la puissance de python.


Les premiers sites web étaient composés de pages HTML stockées dans des fichiers
se trouvant dans un même répertoire. Le serveur web était alors simplement
configuré pour servir tous les fichiers de ce répertoire. C'est ce que
l'on appelle communément un site web statique, c'est-à-dire un site web
composé de pages HTML qui ne changent pas. Ces sites web statiques sont
intéressants pour du contenu tel que ce syllabus qui ne change
que rarement. La plupart des sites web actuels sont dynamiques. Un
programme reçoit les requêtes des utilisateurs et y répond en générant
si nécessaire les pages HTML correspondantes à la volée. Flask permet
de construire un tel site web assez facilement en python.

Avant de se lancer dans l'écriture d'un site web dynamique en flask, il faut
se rappeler que sur le web, toute page est identifiée par son
Uniform Resource Locator (URL). Quand un utilisateur interagit avec
un site web à travers son navigateur, celui-ci charge différentes pages
en utilisant l'HyperText Transport Protocol (HTTP). Le fonctionnement
détaillé de HTTP sort du cadre de ce cours, mais vous devez savoir
qu'un navigateur peut utiliser HTTP de deux façons différentes.

La première est d'envoyer une requête GET HTTP pour un URL particulier. Le
serveur web répond à cette requête en renvoyant au navigateur la page
HTML correspondant à l'URL demandé. L'immense majorité des requêtes qu'un
navigateur fait à un serveur web sont des GET HTTP.

A côté de ces requêtes GET HTTP, un navigateur peut aussi utiliser
des requêtes POST HTTP. Une telle requête n'est utilisée que lorsque le
navigateur veut envoyer de l'information autre qu'un URL au serveur. C'est
par exemple le cas lorsque l'utilisateur remplit un formulaire sur une
page web.

Dans un site web purement statique, le serveur web supporte uniquement
les requêtes GET HTTP. Pour chaque URL demandé, il analyse la partie
fichier de cet URL et si le fichier existe retourne son contenu et
sinon une erreur. Pour illustrer cela, considérons que le serveur
web est configuré pour servir le répertoire ci-dessous. Celui-ci contient
deux fichiers et deux sous-répertoires.


.. code-block:: console

   index.html
   page.html
   css
   images

Le répertoire ``css`` contient le fichier ``style.css`` qui est référencé
par les deux pages HTML. Le répertoire ``images`` contient le fichier ``logo.png``.

Le fichier `index.html` contient la page reprise ci-dessous.


.. literalinclude:: figures/html/exemple.html
   :language: html
	      

Le site web a été configuré pour servir le document `index.html` lorsqu'un
navigateur demande la racine du site web (`/`). Le navigateur reçoit donc
ce fichier en réponse à sa requête GET HTTP. Il lit le contenu du document
HTML et doit directement :

 - faire une requête GET HTTP pour charger la feuille de style (`style.css`)
 - faire une requête GET HTTP pour charger l'image `/images/logo.png`


Si l'utilisateur clique sur le lien vers `page.html`, le navigateur
fera une nouvelle requête GET HTTP pour charger cette page depuis le serveur
et afficher son contenu. L'interaction entre un navigateur web
et un serveur est donc une succession de requêtes HTTP.

flask s'inspire de ce mode de fonctionnement et vous permet d'écrire un
programme en python qui répond aux requêtes HTTP faites par le navigateur.


.. literalinclude:: flask/simple-flask.py
   :language: python

              

flask utilise des décorateurs python pour indiquer l'URL qui doit
être associée à une fonction python. Lorsque le serveur reçoit une
requête GET HTTP qui demande le fichier `/`, il exécute la fonction
`index()` qui retourne le contenu correspondant au fichier `index.html`.
Il en va de même pour la fonction `page()` qui est appelée automatiquement
par le serveur web dès que celui-ci reçoit une requête pour `page.html`.

.. note::

   Dans le cadre de ce premier projet web, nous utiliserons la technologie
   web en local. Le serveur que vous allez développer fonctionnera uniquement
   sur votre ordinateur et ne sera pas accessible depuis Internet. L'écriture
   d'un serveur web dynamique accessible depuis l'Internet nécessite de prendre
   en compte des contraintes au niveau de la sécurité qui sortent du
   cadre de ce cours de première année. 


Avec ces décorateurs et ces fonctions, il est possible de concevoir tout
un site web dynamique qui permet à l'utilisateur d'interagir réellement
depuis son navigateur. Les fonctions que vous écrivez peuvent (doivent ?)
bien entendu faire appel à d'autres fonctions et suivant les bonnes habitudes
de découpe d'un programme en petites fonctions simples qui sont documentées,
testées et réutilisables. 
