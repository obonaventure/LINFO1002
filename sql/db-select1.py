#!/usr/bin/env python

import sqlite3

# Accès à la base de données

conn = sqlite3.connect('Eleves.sqlite')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

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
# utilisation de la base de données

#start

print("Prénom\t Nom")
for row in cursor.execute("SELECT PRENOM, NOM from CLASSE"):
    print(row[0], "\t", row[1])


#end

#s1


for row in cursor.execute("SELECT * from CLASSE"):
    print(row)

#e1

#s2


for row in cursor.execute("SELECT * from CLASSE WHERE POINTS>70"):
    print(row)

#e2

#s3

for row in cursor.execute("SELECT AGE from CLASSE "):
    print(row)

#e3
#s4

for row in cursor.execute("SELECT DISTINCT AGE from CLASSE "):
    print(row)

#e4

#s5

for row in cursor.execute("SELECT NOM, MATRICULE from CLASSE WHERE POINTS IS NULL"):
    print(row)

#e5
#s6
print ("Requête : Du%")
for row in cursor.execute("SELECT NOM, PRENOM from CLASSE WHERE NOM LIKE 'Du%'"):
    print(row)
print ("Requête : Du%t")
for row in cursor.execute("SELECT NOM, PRENOM from CLASSE WHERE NOM LIKE 'Du%t'"):
    print(row)
print ("Requête : D_____t")
for row in cursor.execute("SELECT NOM, PRENOM from CLASSE WHERE NOM LIKE 'D____t'"):
    print(row)
    
#e6

#e5
#s7

for row in cursor.execute("SELECT NOM, POINTS+10 from CLASSE"):
    print(row)

#e7

#s8

for row in cursor.execute("SELECT 'Etudiants', avg(POINTS) from CLASSE"):
    print(row)
    # Affiche ('Etudiants', 76.93333333333334)

for row in cursor.execute("SELECT count(*) from CLASSE WHERE NOM LIKE 'D%'"):
    print(row)
    # Affiche (3,)

for row in cursor.execute("SELECT max(POINTS) from CLASSE "):
    print(row)
    # Affiche (88.65,)

for row in cursor.execute("SELECT group_concat(NOM,'/') from CLASSE WHERE NOM LIKE '%t'"):
    print(row)
    # Affiche ('Durant/Dupont',)

#e8

#s9

for row in cursor.execute("SELECT count(DISTINCT(NOM)) from CLASSE"):
    print(row)

#e9







# Si on a fait des modifications à la base de données
conn.commit()

# Toujours fermer la connexion quand elle n'est plus utile
conn.close()
