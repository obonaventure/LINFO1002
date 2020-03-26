.. LINFO1002 documentation master file, created by
   sphinx-quickstart on Tue Jan 28 18:06:33 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. spelling::

   crashé
   anonymisée
   d'INGINIOUS
   téléchargeable
   tutoriel
   l'UCLouvain
   l'Internet
   l'URL
   l'HyperText
   grading
   frontend

   
Second projet: site web de visualisation
========================================


Durant le premier projet, vous avez proposé de nouveaux exercices en
python pour la plate-forme `INGINIOUS <https://www.inginious.org>`_.
Sur la plate-forme INGINIOUS qui
est déployée à l'UCLouvain, des milliers d'étudiants soumettent chaque
semaines des dizaines de milliers de propositions de réponses à des
exercices de programmation. Durant l'année 2019, plus de trois mille
étudiants ont fait ensemble plus de 800.000 soumissions. INGINIOUS
intègre quelques visualisations qui permettent aux enseignants de
suivre la progression des étudiants dans leur cours.

La première de ces visualisations est accessible via l'onglet `Stats` de
INGINIOUS. Elle permet de visualiser le nombre de soumissions faites pour
un cours donné.

.. figure:: figures/inginious-stats-1.png

   Statistiques de base sur INGINIOUS	    


L'onglet `Reporting` fournit également quelques rapports sur les
résultats de différentes tâches.

.. figure:: figures/inginious-stats-2.png

   Un exemple de rapport fourni par INGINIOUS	    


La plupart des enseignants souhaitent disposer de rapports plus complets
qui intègrent une visualisation graphique. Même si il est écrit en
Python et est `disponible en open-source <https://github.com/UCL-INGI/INGInious>`_, une modification directe
du code source d'INGINIOUS sort du cadre de ce cours. Nous allons nous 
contenter de préparer un prototype de visualisation des résultats
INGINIOUS.

Pour cela, une partie des données collectées l'an passé sur INGINIOUS
a été convertie
dans une base de données au format SQL. Cette base de données occupe
près de 100 MBytes tout en ne contenant que l'information relative
à trois cours disponibles sur la plate-forme.

Afin d'aider les enseignants qui utilisent INGINIOUS, votre objectif
est de concevoir et d'implémenter un site web interactif permettant de
visualiser de façon claire la progression et les résultats obtenus par
les étudiants. Ce faisant, vous aller devoir apprendre les concepts
suivants:

 - les bases du fonctionnement du world-wide web, voir :ref:`ref-web` 
 - les bases de l'HyperText Markup Langage (HTML) qui est utilisé pour écrire les pages disponibles sur un serveur web, voir :ref:`ref-html`
 - les bases pour utiliser la librairie ``chart.js`` pour produire facilement de belles visualisations, voir :ref:`ref-chartjs`
 - le framework Flask qui permet d'implémenter facilement des sites web interactifs en python, voir :ref:`ref-flask`
 - les bases de SQL et la façon dont on peut interagir avec une base de données SQL en python, voir :ref:`ref-sql`

Vous veillerez, bien entendu, à écrire du code python clair, documenté et accompagné de tests unitaires. Une première version de votre projet devra être prête avant la fin du mois d'avril. Début mai, vous fournirez du feedback détaillé à d'autres groupes d'étudiants. Ensuite vous utiliserez le feedback reçu pour améliorer votre propre projet et présenterez votre prototype à l'équipe enseignante et un des développeurs d'INGINIOUS.


La base de données extraite d'INGINIOUS est composée de deux tables et a la structure suivante :

.. code-block:: python

   submissions_schema = """CREATE TABLE submissions (
      id            INTEGER PRIMARY KEY, /* ID numérique */
      course        TEXT,                /* ID du cours */
      task          TEXT,                /* ID de la tâche */
      status        TEXT,                /* Etat du grading (done ou error), error indique que la soumission n'a pas pu être traitée */
      submitted_on  TEXT,                /* Date de soumission en ISO8601 UTC */
      username      TEXT,                /* ID de l'étudiant anonymisé */
      response_type TEXT,                /* Type du feedback (peu utile) */
      grade         REAL,                /* Note obtenue */
      result        TEXT                 /* failed, killed, success, overflow, timeout, crash, error ou NULL */
   );"""

   user_tasks_schema = """CREATE TABLE user_tasks (
      id         INTEGER PRIMARY KEY, /* ID numérique */
      course     TEXT,                /* ID du cours */
      task       TEXT,                /* ID de la tâche */
      username   TEXT,                /* ID de l'étudiant anonymisé */
      grade      REAL,                /* Note obtenue pour la soumission considérée pour l'évaluation */
      submission INTEGER,             /* ID de la soumission considérée pour l'évaluation */
      succeeded  TEXT,                /* true ou false, indiquant si la tâche est réussie (indépendamment de grade) */
      tried      INTEGER,             /* Le nombre d'essais de l'étudiant pour la tâche */
   FOREIGN KEY (submission) REFERENCES submissions(id)
   );
   """ 

   
Cette base de données a été anonymisée, vous n'avez pas accès aux vrais noms des étudiants. La plupart des champs ont une signification qui peut être comprise directement sur base du commentaire. Le champ ``result`` de la première table comprend les valeurs suivantes:

 - `failed`: La soumission a été évaluée et l'étudiant a raté
 - `killed` : le job de grading a été tué
 - `success`: La soumission a été évaluée et l'étudiant a réussi
 - `overflow`: L'évaluation de la soumission de l'étudiant a dépasser la mémoire allouée
 - `timeout` : L'évaluation de la soumission de l'étudiant a dépasser le temps imparti
 - `crash` : L'évaluation a crashé
 - `error` : Le frontend a rencontré une erreur d'un type inconnu 

La base de données est téléchargeable depuis :download:`sql/inginious.sqlite`
   
Continuez votre lecture avec le document :doc:`web`.

