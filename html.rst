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


.. code-block:: html
                
   <!DOCTYPE html>
   <html>
    <head>
     <meta charset="utf-8">
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

Lorsque l'on écrit des pages HTML dans un éditeur de textes, il est parfois
utile d'ajouter des commentaires. Par convention, dans un document HTML, un
commentaire s'écrit à l'intérieur d'une balise `<!-- ... -->`. Il faut noter
que la fin du commentaier ne comprend pas de caractère `\` contrairement
aux balises fermantes habituelles. Un commentaire peut être placé sur
une ligne ou couvrir plusieurs lignes, comme les commentaires dans les
langages de programmation.

.. code-block:: html
                
   <!DOCTYPE html>
   <html>
    <head>
     <meta charset="utf-8">
     <title>Titre de page</title>
     <!-- Un commentaire dans l'entête -->
    </head>
    <body>
     <!-- Un commentaire dans le corps -->
     <h1>Première section</h1>
     <!--   commentaire
           <p>Un petit paragraphe.</p>
           <h1>Seconde section</h1>
     -->       	   
     <p>Un paragraphe.</p>
    </body>
   </html>

Comme le langage HTML utilise les caractères `<` et `>` dans la définition
des balises, comment faut-il afficher ces caractères dans un document
HTML ? Il n'est pas possible de simplementation utiliser ces caractères
puisqu'ils sont interprétés par HTML comme des débuts de balises. Pour résoudre
ce problème, HTML définit les entités caractères suivantes:

 - `&lt;` pour représenter le caractère `<` dans du texte
 - `&gt;` pour représenter le caractère `>` dans du texte
 - `&amp;` pour représenter le caractère `&` dans du texte
 - `&nbsp;` pour indiquer un espace inséquable
 - `&quot;` pour le caractère correspondant aux guillemets (`"`)
 - `&apos;` pour le caractère correspondant à l'apostrophe


Ainsi, dans une page HTML, il est possible d'expliquer en HTML le format d'un
commentaire en HTML.

.. code-block:: html
                
   <!DOCTYPE html>
   <html>
    <head>
     <meta charset="utf-8">
     <title>Ceci est un titre</title>
    </head>
    <body>
     <p>
     &lt;!-- Un commentaire disant que 3 &lt; 5  --&lg;
     </p>
    </body>
   </html>


De nombreuses balises HTML supportent des attributs qui permettent de
préciser certains paramètres de chacune d'entre elles. Il est impossible
de les lister toutes dans ce document. En voici quelques unes
qui pourraient être utiles dans le cadre de ce projet.

La balise `<html>` support l'attribut `lang` qui permet d'indiquer la langue
dans laquelle la page a été écrite. Ainsi `<html lang="fr">` est la balise
ouvrante d'un document écrit en français tandis que `<html lang="en">`
est celle d'un document en anglais.

La balise `<meta>` que l'on retrouve
dans l'entête d'un document HTML supporte différents attributs. Le plus important est le type de code
de caractères utilisé pour écrire le document. Aujourd'hui, le codage
le plus répandu est l'Unicode qui correspond à UTF-8. Parmi les autres
attributs, on peut citer :

 - l'attribut `description` qui fournit une information sur le contenu de la page
 - l'attribut `keywords` qui indique les mots-clés et peut être utile à des moteurs de recherche
 - l'attribut `author` qui indique l'auteur de la page

.. code-block:: html   

   <head>
     <meta charset="UTF-8">
     <meta name="description" content="Une première page web">
     <meta name="keywords" content="HTML,exemple">
     <meta name="author" content="Jean Tartempion">
   </head>

   

Ces attributs aux balises HTML nous permettent d'aborder deux éléments clés des
pages HTML :

 - les liens hypertextes
 - les images


En HTML, un lien hypertexte s'écrit en utilisant la balise `<a>...</a>` pour
ancre (`anchor` en anglais) et en utilisant l'attribut `href` pour indiquer
l'URL du lien hypertext. Ainsi dans un document HTML, un lien qui
pointe vers le site web de l'UCLouvain s'écrit comme suit :

.. code-block:: html

   <p>
   Allez visiter <a href="https://www.uclouvain.be"> le site web de l'UCLouvain</a>.
   </p>

Grâce à la balise `<img>`, il est possible d'inclure une image à n'importe
quel endroit dans une page HTML. Cette balise support plusieurs attributs :

 - `src` : permet d'indiquer l'URL du fichier contenant l'image à inclure. Celui-ci peut être absolu ou relatif. La plupart des navigateurs supportent les fichiers aux format `png`, `jpg` ou `svg`.
 - `alt` : (optionnel) permet d'indiquer une description textuelle de l'image pour les navigateurs non-graphiques
 - `width` : (optionnel) permet d'indiquer la large de l'image en pixels. Par défaut le navigateur prendra la largeur de l'image d'origne
 - `height` : (optionnel) permet d'indiquer la hauteur de l'image en pixels. Par défaut le navigateur prendra la hauteur de l'image d'origne   


Dans la document HTML, l'attribut `src` d'une image peut correspondre à
un fichier se trouvant dans le même répertoire que le document HTML, un
fichier présent dans un autre répertoire du même serveur ou sur un
autre serveur. En pratique, les designers de sites web regroupent
souvent leurs images dans un ou quelques répertoires voir utilisent des
serveurs dédiés pour les sites utilisant de très nombreuses images. Pour
un petit site, le plus simple est de regrouper toutes les images
du site dans un répertoire nommé par exemple `/images`.
   
.. code-block:: html

   <!-- Une image dans le même répertoire ->
   <img src="image.jpg" alt="Une image" width="500" height="600">

   <!-- Une image dans un autre répertoire ->
   <img src="/images/photo.jpg" alt="Une photo" width="200" height="200">

   <!-- Une image sur un autre serveur ->
   <img src="https://uclouvain.be/sites/all/themes/ucltheme/logo.png" alt="Le logo de l'UCLouvain">

   

Dans un article scientifique, les figures sont généralement accompagnées
d'une légende. C'est aussi possible en HTML avec les balises `<figure>` et
`<figcaption>`.

.. code-block:: html

   <figure>
    <img src="/images/mesures.jpg" alt="Mesures récentes" width="500" height="600">
    <figcaption>Les mesures collectées ce matin</figcaption>
   </figure>
   
   
HTML permet également d'écrire des listes ordonnées ou non. Les listes
ordonnées utilisent la balise `<ol>` tandis les non-ordonnées utilisent la
balise `<ul>`. Ces deux balises supportent différents attributs. Pour la
liste non-ordonnée, l'attribut `list-style-type` indique le type de marqueur
d'élément. Par défaut c'est un point, mais il est possible d'utiliser
un cercle (attribut `circle`), un carré (attribut `square`).

.. code-block:: html

   Les nombres premiers		
   <ul style="list-style-type:circle">
    <li>1</li>
    <li>2</li>
    <li>3</li>
    <li>5</li>
   </ul>


Les listes ordonnées supportent elles l'attribut `type` qui permet
de spécifier le type de numérotation des éléments. Par défaut c'est
la numérotation entière qui est utilisée, mais HTML supporte aussi l'utilisation
de lettres majuscules (attribut `type="A"`), minuscules (attribut `type="a"`)
ou en chiffres romains (attribut `type="I"`).

.. code-block:: html

   Des villes d'Italie		
   <ol style="type:I">
    <li>Rome</li>
    <li>Milan</li>
    <li>Naples</li>
    <li>Turin</li>
   </ol>


Outre les listes, il est aussi possible de présenter des informations
sous la forme de tables. Les tables utilisent quatre types de balises.
La balise `<table>` marque le début d'une table. A l'intérieur d'une
table la balise `<tr>` est utilisée pour représenter une ligne (`table row`
en anglais). La balise `<th>` est utilisée pour un nom ou une entête de colonne
(`table header` en anglais) et enfin la balise `<td>` entoure une donnée
dans une cellule de la table.

.. code-block:: html

   <table>
    <tr>
     <th>Pays</th>
     <th>Continent</th>
     <th>Capitale</th>
    </tr>
    <tr>
     <td>Belgique</td>
     <td>Europe</td>
     <td>Bruxelles</td>
    </tr>
    <tr>
     <td>Japon</td>
     <td>Asie</td>
     <td>Tokyo</td>
    </tr> 
   </table>


Il est possible en utilisant les attributs de ces balises de contrôler
finement la façon dont les données sont présentées dans une table.
Vous trouverez plus d'informations à ce sujet dans les références
mentionnées au début du chapitre.

Il existe de très nombreux autres attributs en HTML5. L'attribut `style`
permet contrôler la couleur, la police utilisée pour afficher du texte et
sa taille ou l'alignement du texte. Voici un exemple simple.

.. code-block:: html

   <h1 style="font-family:courrier;">Une entête en police courrier</h1>
   <p style="color:blue;text-align:center;">Ce paragraphe est écrit en couleur bleue et centré.</p>


Il est aussi possible de contrôler la couleur du fond (`background-color`) et
la taille de la police (`font-size`). HTML5 supporte de très nombreuses couleurs. Les plus courantes sont identifiées par un nom. Voir `https://www.w3schools.com/colors/colors_names.asp <https://www.w3schools.com/colors/colors_names.asp>`_ pour plus de détails. Il est aussi possible de préciser la couleur demandée
sur base de ses composantes rouge, verte et bleue. Cela permet à HTML de
supporter toutes les couleurs imaginables.

.. formulaire ??

Lorsque l'on développe quelques pages HTML manuellement, il est possible
d'indiquer ces attributs directement dans chaque page HTML. Malheureusement,
c'est assez fastidieux et il est difficile de garder une cohérence
entre la présentation des différentes pages d'un même site web. Lorsqu'un
site web est géré par un logiciel et est succeptible d'afficher de nombreuses
pages HTML, il est préférable d'utiliser des feuilles de style ou Cascading
Style Sheets (CSS). Une feuille de style est un ensemble cohérent
de règles que le navigateur va appliquer à la mise en page d'un document
HTML. Elle peut être incluse directement dans l'entête de chaque page HTML ou
référencée dans cette entête. La seconde solution est la préférable. Cela
permet à avoir une même feuille de style, chargée une seule fois par le
navigateur, pour toutes les pages d'un site web. C'est la solution que
nous vous encourageons à adopter et donc la seule que nous
décrivons dans ces notes.

Une feuille de style indique comment la page sera présentée globalement (police
de caractères, couleur de fond d'écran, ...) mais surtout comment chaque élément
de la page sera présenté. Dans une feuille de style CSS, il est possible de
modifier la présentation des entêtes d'un niveau particulier, des paragraphes,
des tables, ... Une feuille style CSS permet d'appliquer une série d'attributs
à des éléments d'un type particulier. La syntaxe générale d'une
feuille de style CSS est :

.. code-block:: css

   /* commentaire sur une ligne */		
   selecteur1 {
     proprieteA: valeurA;
     proprieteB: valeurB;
     /* ... */
   }
   /*
    * Commentaire
    * sur plusieurs lignes
    */
   selecteur2 {
     proprieteX: valeurX;
     proprieteY: valeurY;
     /* ... */
   }


Dans une telle feuille de style, le sélecteur correspond à un type d'élément
se trouvant dans le document HTML. L'élément `body` correspond à l'ensemble
du corps de la page HTML. L'élément `p` correspond à un paragraphe tandis
que l'élément `h1` un titre de premier niveau. Dans une feuille CSS,
la balise `/*` marque le début d'un commentaire. La balise `*/` marque la
fin d'un commentaire.

.. code-block:: css

   /* les titres en bleu et les paragraphes en noir */
   h1 {
    color: blue;
   }
   p {
    color: black;
   }

   
La puissance de CSS dans HTML5 vient du fait qu'il est possible d'appliquer
ces attributs à des parties de texte qui ont étés préalablement marquées
par l'auteur du document. Prenons comme exemple une application web
qui doit afficher une liste de lieux et une liste de mesures de températures
minimales et maximales. Supposons que le nom du lieu doit s'afficher en
bleu et les températures en vert. Sans les styles, une telle page
en HTML pourrait s'écrire comme suit:

.. code-block:: html

   <ul>
    <li style="color:blue">Paris</li>
      <ul>
        <li style="color:green">Min: 5°</li>
	<li style="color:green">Max: 9°</li>
      </ul>
    <li style="color:blue">Naples</li>
      <ul>
        <li style="color:green">Min: 17°</li>
	<li style="color:green">Max: 22°</li>
      </ul>
  </ul>    

Avec une feuille de style, il est plus simple de d'abord identifier chaque
type d'élément. Cela peut se faire en utilisant l'attribut `class` qui
permet d'identifier des sous-types d'un même type.

.. code-block:: html

   <ul>
    <li class="ville">Paris</li>
      <ul>
        <li class="temp">Min: 5°</li>
	<li class="temp">Max: 9°</li>
      </ul>
    <li style="color:blue">Naples</li>
      <ul>
        <li class="temp">Min: 17°</li>
	<li class="temp">Max: 22°</li>
      </ul>
  </ul>    


L'attribut `class` de chaque élément `<li>` n'est pas directement affiché
par le navigateur, mais il est utilisé par le CSS ci-dessous.

.. code-block:: css

   /* les villes titres en bleu et les températures en vert */
   li.ville {
    color: blue;
   }
   li.temp {
    color: green;
   }

   
L'avantage clair de cette approche est que si on veut remplacer la
couleur verte par de l'orange pour les températures, il suffira
de modifier une seule ligne dans le fichier CSS.
