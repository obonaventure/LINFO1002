#!/usr/bin/env python

import sqlite3

# Accès à la base de données

conn = sqlite3.connect('Eleves.sqlite')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

# utilisation de la base de données
#start

cursor.execute('''CREATE TABLE CLASSE
         (MATRICULE INT PRIMARY KEY     NOT NULL,
         NOM           TEXT    NOT NULL,
         PRENOM           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         POINTS          REAL);''')

#end
# Si on a fait des modifications à la base de données
conn.commit()

# Toujours fermer la connexion quand elle n'est plus utile
conn.close()
