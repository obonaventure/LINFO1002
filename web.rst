.. LINFO1002 documentation master file, created by
   sphinx-quickstart on Tue Jan 28 18:06:33 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _ref-web:
   
Le world wide web (www)
=======================

Inventé durant les années 1990s par les physiciens du Centre Européen de
Recherche Nucléaire (CERN) à Genève, le world wide web (www) est petit
à petit une des composante fondamentale de la société de l'information
que nous connaissons aujourd'hui. A l'origine, le www a été conçu de façon
à faciliter le partage de documents scientifiques. Dans un document
scientifique, il est très courant de citer d'autres documents que ce soit
via des notes de bas de pages ou des citations dans une bibliographie reprise
à la fin du document. Les inventeurs du web ont voulu faciliter l'accès à ces
documents en les structurant comme des `hypertextes`.

L'idée d'un document hypertexte est plus ancienne puisqu'elle remonte aux années
soixante avec le projet Xanadu. Un document hypertexte est un document qui
contient des références vers un autre document. Dans un hypertexte, ces
références sont telles que le lecteur peut aisément passer d'un document à sa
référence par un simple clic de souris. Les premiers hypertextes étaient
stockés sur un ordinateur isolé et nécessitaient l'utilisation de logiciels
spécifiques pour les visualiser. Avant l'invention du web, le logiciel
Hypercard disponible sur les premiers Mac de chez Apple était un des rares
hypertextes à être connus du grand public. L'invention du web a permis de construire des documents hypertextes qui sont stockés sur des ordinateurs différents
et même des documents qui combinent des parties de documents stockées sur
différents ordinateurs.

Les détails du fonctionnement du www sortent du cadre de ce cours et seront abordés dans le cours de `réseaux informatiques <https://www.computer-networking.info>`_ en troisième année de bachelier. Dans le cadre de ce projet, nous nous limiterons au base de fonctionnement du web. Le web repose sur trois éléments
principaux:

 - un langage (HTML) permettant de décrire des pages d'hypertextes
 - un protocole (HTTP) permettant à un navigateur web de charger un document HTML depuis un ou plusieurs serveurs web
 - un mécanisme (URL) permettant d'identifier de façon non-ambigüe une document web
  
Ces trois éléments sont supportés par les navigateurs et serveurs web. Ceux-ci jouent un rôle important dans l'évolution du web et le web n'aurait pas eu le succès qu'il a aujourd'hui sans l'existence de navigateurs et de serveurs efficaces. Le CERN a développé le premier navigateur textuel et le premier serveur. Ces deux logiciels étant open-source, ils ont servis de base au développement des autres navigateurs et serveurs web. Le navigateur Mosaic, développé par le National Center for Supercomputing Applications (NCSA) a été le premier navigateur graphique capable d'intégrer des images dans les documents. Netscape, créé par l'équipe qui avait lancé Mosaic, a été le premier navigateur commercial. C'est Netscape qui a été la première société à proposer des solutions pour sécuriser
le commerce électronique. Les navigateurs actuels sont Firefox de Mozilla, Safari chez Apple et Chrome développé par Google. Microsoft a récemment annoncé que leur nouveau navigateur serait basé sur le coeur de Chrome qui est open-source et utilisé par d'autres navigateurs tels que brave. Côté serveurs, le serveur
premier serveur développé par le CERN a été petit à petit amélioré par
de nombreux développeurs qui diffusaient leurs modifications sous forme
de `patches`. Après quelques temps, un groupe de développeurs a décidé de regrouper les patches les plus populaires dans un nouveau projet baptisé `Apache`,
dont le nom reste fort proche du mot `patches`. Il reste aujourd'hui un serveur web très populaire avec d'autres dont ``nginx`` par exemple.

Sur le réseau Internet, un serveur est identifié par un nom et une adresse IP.
Le nom est important pour l'utilisateur car c'est celui qu'il utilise dans
son navigateur web pour contacter un serveur. L'adresse IP est
utilisée par les ordinateurs pour s'échanger de l'information. Il existe un
service (le Domain Name System - DNS) qui permet d'obtenir
l'adresse IP qui correspond à un nom de machine, mais nous n'entrerons
pas dans ces détails dans le cadre de ce projet.

Il y a aujourd'hui deux types d'adresses sur Internet:

 - les adresses IP version 4 sur 32 bits. Celles-ci sont généralement représentées sous la forme de quatre entiers séparés par le caractère ``.`` Ainsi ``193.191.245.244`` est l'adresse IP version 4 qui correspond au nom ``www.belgium.be`` 
 - les adresses IP version 6 sur 64 bits. Celles-ci sont généralement représentées sous la forme d'une suite de nombres en notations hexadécimale séparés par le caractère ``:`` Ainsi, ``2a01:690:35:100::f5:f4`` est l'adresse IP version 6 qui correspond au nom ``www.belgium.be`` 

Au niveau des noms de machine, les informaticiens ont l'habitude de donner
des noms qui sont liés au service rendu par un service donné. Ainsi, dans une
petite entreprise, il sera fréquent d'utiliser le nom ``print`` pour le
serveur d'impressions et ``www`` pour le serveur web de l'entreprise. De
nombreuses entreprises ont choisi d'adopter ces conventions. Si leurs réseaux
sont isolés, le PC de l'entreprise A ne pourra rejoindre qu'un seul serveur
baptisé ``www``. Si par contre toutes ces entreprises sont connectées à l'Internet, il faut absolument que l'on évite d'associer le même nom à plusieurs
serveurs. 

La façon standard de s'assurer de l'unicité des noms de machine sur Internet est
de construire ces noms de machine de façon hiérarchique. En simplifiant, un
nom de machine sur Internet est composé de deux parties:

 - le nom de la machine qui n'est pas nécessairement unique
 - le nom du domaine dans lequel la machine se trouve qui lui est unique

Le nom complet d'une machine est la concaténation entre le nom de la machine
et le domaine dans lequel la machine se trouve. Les noms de domaine sont
attribués de façon hiérarchique. Chaque pays dispose d'un nom de domaine en
deux lettres (``be`` pour la Belgique, ``fr`` pour la France, ...). Quand
une entreprise belge veut obtenir un nom de domaine, elle contacte le
secrétariat qui gère le domaine ``.be``. Celui-ci vérifie si le nom demandé par
l'entreprise est déjà utilisé et si non, il est réservé pour l'entreprise qui
peut l'utiliser pour nommer ses ordinateurs. 
   
Les noms de domaine jouent un rôle clé dans la définition des Uniform Ressource Locators (URL). Un URL est une sorte d'adresse pour un document accessible sur un serveur web. Tout document accessible via un serveur web est identifié par un URL. Un URL est une chaîne de caractères qui est composée de différentes parties:

 - un identifiant de protocole permettant de télécharger le document suivi de ``://``
 - un nom de domaine suivi du caractère ``/``
 - un nom de fichier


Le web supporte différents identifiants de protocoles. Les plus utilisés sont ``http`` et ``https``. Dans le cadre de ce projet, nous utiliserons ``http``. La plupart des serveurs Internet utilisent ``https`` qui est la version sécurisée de ``http``. La distinction entre ces deux protocoles sort du cadre de ce projet.

Prenons quelques exemples pour comprendre d'utilisation des URLs. Nous verrons qu'ils jouent un rôle important dans le langage HTML également. Pour bien comprendre comment fonctionnent ces URLs, il est intéressant de prendre quelques exemples.

Commençons par le site web de l'UCLouvain. Celui-ci est accessible en français et en anglais. La version française utilise l'URL ``https://uclouvain.be/fr/index.html`` tandis que la version anglais est accessible via ``https://uclouvain.be/en/index.html``. L'URL de la page en français indique que celle-ci peut être chargée en contactant le serveur ``uclouvain.be`` en utilisant le protocole ``https``. Sur ce serveur, le document demandé est ``fr/index.html``. Ce document correspond au fichier dénommé ``index.html`` dans le répertoire ``fr``. Sur le même site, l'URL ``https://uclouvain.be/fr/etudier/bacheliers.html`` correspond à la page consacrée aux études de bachelier. Celle-ci est dans le fichier ``bachelier.html`` qui se trouve dans le sous-répertoire ``etudier`` du répertoire ``fr``.

La structuration d'un site web en répertoires et sous-répertoires est très fréquente. Nous verrons qu'elle sera utile lors de la création de pages en format HTML et aussi lorsque nous utiliserons flask pour créer notre site web interactif.

 



