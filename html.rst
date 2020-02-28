.. LINFO1002 documentation master file, created by
   sphinx-quickstart on Tue Jan 28 18:06:33 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Le langage HTML
===============

L'HyperText Markup Langage (HTML) est un langage de description de documents
qui s'appuie sur un ensembles de balises (`markups` en anglais). Il existe de
nombreux livres et sites web qui fournissent de très nombreux détails sur HTML.

Dans le cadre de ce projet, nous nous concentrerons sur un sous-ensemble de
la version 5 du langage HTML (HTML5). Libre à vous d'explorer le web et les
bibliothèques pour utiliser d'autres fonctionnalités de ce langage. Il est
très important pour un informaticien et pouvoir apprendre de façon autonome
en s'aidant des multiples ressources disponibles. 

Un document HTML est composé de deux parties : l'entête (`head` en anglais) et le corps (`body`en anglais). L'entête contient des informations telles que le titre de la page qui sera affiché en haut de la fenêtre du navigateur, mais aussi le type de codage des caractères utilisé, ... Le corps de
la page contient lui le document en hypertexte.

Tout document HTML commence par la chaîne de caractères ``<!DOCTYPE html>``. Cette chaîne est suivie par la première balise (ouvrante) : `<html>`. Dans
l'exemple ci-dessous, tout le texte se trouvant entre la balise ouvrante, `<html>`, et la balise fermante, `</html>` est marqué comme étant en HTML. Si un document HTML contient la balise ouvrante `<xyz>` il doit y avoir une balise fermante `</xyz>` plus loin qui délimite la zone de texte couverte par cette balise. C'est un peu comme des parenthèses dans une expression mathématique. Il y a toujours une parenthèse fermante qui correspond à une parenthèse ouvrante. 

L'entête du document HTML ci-dessous est la zone du fichier se trouvant entre
les balises `<head>` et `</head>`. Celle-ci ne contient que le titre de la page que l'on reconnait grâce à l'utilisation de la balise `<title>`.


.. code-block:: console
                
   <!DOCTYPE html>
   <html>
    <head>
     <title> Un beau titre </title>
    </head>
    <body>
     <h1>Première section</h1>
     <p>Un petit paragraphe.</p>
     <h1>Seconde section</h1>
     <p>Un autre paragraphe.</p>
    </body>
   </html>


Le corps du document HTML ci-dessus est la partie du fichier se trouvant entre
les balises `<body>` et `</body>`. Ce texte comprend deux sous-sections contenant chacune un paragraphe. La balise `<h1>` correspond à un titre de section de premier niveau (`<h2>` pour une sous-section, c'est-à-dire un titre de deuxième niveau, ...). La balise `<p>` sert à identifier un paragraphe.

HTML5 définit de nombreuses balises qui ne peuvent pas être toutes détaillées dans le cadre de cette brève introduction. Outre les balises telles que `<h1>`
qui définissent des niveaux de titre, il existe des balises qui permettent de
modifier le style utilisé pour présenter certains mots à l'écran, dont :

 - `<b>` qui est utilisé pour indiquer que du texte doit être écrit en gras. `<strong>` est un synonyme sur de nombreux navigateurs.
 - `<i>` qui est utilisé pour indiquer que du texte doit être écrit en italique. `<em>` est un synonyme sur de nombreux navigateurs.
 - `<sub>` qui indique que du texte doit être mis en indice
 - `<sup>` qui indique que du texte doit être mis en exposant
 - `<mark>` qui indique que du texte doit être surligné

Certaines balises sont liées à la présentation des paragraphes. Comme indiqué
précédemment, un paragraphe début toujours par `<p>` et se termine par `</p>`. Celui-ci peut contenir de nombreuses lignes de textes. Le navigateur se chargera
de mettre en forme le paragraphe correctement entre les balises `<p>` et `</p>`.
Parfois, l'auteur d'une page HTML peut souhaiter forcer un retour à la ligne à un endroit particulier d'un paragraphe. Cela peut se faire en utilisant
la balise ouvrante `<br>`. Cette balise force le navigateur à aller directement
à la ligne. C'est une des rares balises HTML à ne pas avoir de balise fermante.

Dans certains cas, notamment pour présenter du code dans un langage de programmation à l'intérieur d'une page HTML, il est préférable que le navigateur
présente le texte tel qu'il a été écrit dans le fichier et sans rajouter
d'espaces ou de retours à la ligne. Cela se fait en utilisant les
balises `<pre>` et `</pre>`. Le texte se trouvant entre ces deux balises
sera alors affiché tel quel en utilisant une police avec espacement fixe entre
les caractères alors que la police standard est généralement avec espacement
proportionnel.
<p>
<pre>
<br>
