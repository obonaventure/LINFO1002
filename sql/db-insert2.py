#!/usr/bin/env python

import sqlite3

# Accès à la base de données

conn = sqlite3.connect('Eleves.sqlite')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

# utilisation de la base de données
#s1

# Encodage direct des données 

cursor.execute('''INSERT INTO CLASSE (MATRICULE, NOM, PRENOM, AGE, POINTS)
                  VALUES (1, 'Durant', 'Emilie', '8', 73.5)''')

#e1
#s2
# Données passées via des espaces réservés

mat=2
nom="Durand"
prenom="Joséphine"
age=7
moyenne=88.65

cursor.execute('''INSERT INTO CLASSE (MATRICULE, NOM, PRENOM, AGE, POINTS)
                VALUES (?, ?, ?, ?, ?)''',
               (mat,nom,prenom,age,moyenne) )
#e2
#s3
# Données passées via des espaces nommés

mat=4
nom="Tartempion"
prenom="Jean"
age=9
moyenne=68.65

cursor.execute('''INSERT INTO CLASSE (MATRICULE, NOM, PRENOM, AGE, POINTS)
                VALUES (:mat, :nom, :prenom, :age, :points)''',
               {"mat":mat,"nom":nom,"prenom":prenom,"age":age,"points":moyenne} )


#e3
# Données incomplètes
#s4
cursor.execute('''INSERT INTO CLASSE (MATRICULE, NOM, PRENOM, AGE)
                  VALUES (12, 'Dupont', 'Jules', 9)''')

#e4
#s5
cursor.execute('''INSERT INTO CLASSE (MATRICULE, NOM, PRENOM)
                  VALUES (9, 'Dupont', 'Emile')''')

# fails:
# Traceback (most recent call last):
#  File "db-insert2.py", line 49, in <module>
#    VALUES (9, 'Dupont', 'Emile')''')
# sqlite3.IntegrityError: NOT NULL constraint failed: CLASSE.AGE

#e5


# Si on a fait des modifications à la base de données
conn.commit()

# Toujours fermer la connexion quand elle n'est plus utile
conn.close()
