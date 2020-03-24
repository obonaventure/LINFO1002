#!/usr/bin/env python

import sqlite3

# Accès à la base de données

conn = sqlite3.connect('Chinook_Sqlite.sqlite')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

#s1
print("Table Artist")
i=0
for row in cursor.execute("SELECT ArtistId, Name FROM Artist "):
    if i<10:
        print(row)
    i=i+1

print("Nombre total de lignes: ",i)
#e1

#s1b
print("Table Artist")
for row in cursor.execute("SELECT ArtistId, Name FROM Artist LIMIT 10"):
    print(row)
#e1b


#s2
print("Table Album")
i=0
for row in cursor.execute("SELECT AlbumId, Title, ArtistId FROM Album "):
    if i<10:
        print(row)
    i=i+1

print("Nombre total de lignes: ",i)        
#e2
        


#s3
print("Table Track")
i=0
for row in cursor.execute("SELECT TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice FROM Track "):
    if i<10:
        print(row)
    i=i+1
print("Nombre total de lignes: ",i)
        
#e3

#s4
print("Albums d'AC/DC")
i=0
for row in cursor.execute("SELECT Title FROM Album WHERE ArtistId=1 "):
    if i<10:
        print(row)
    i=i+1
print("Nombre total de lignes: ",i)
        
#e4

#s5
print("Albums d'AC/DC ou Aerosmith")
i=0
for row in cursor.execute("SELECT Title FROM Album WHERE ArtistId in (1, 3) "):
    if i<10:
        print(row)
    i=i+1
print("Nombre total de lignes: ",i)
        
#e5

#s6
print("Ids des artistes dont le nom débute par A")
artistes=[]
for row in cursor.execute("SELECT ArtistId FROM Artist WHERE Name LIKE 'A%'"):
    artistes.append(row[0])
    
print(artistes)
print("Albums d'artistes dont le nom débute par A")
i=0
for row in cursor.execute("SELECT Title FROM Album WHERE ArtistId in {}".format(tuple(artistes))):
    if i<10:
        print(row)
    i=i+1
print("Nombre total de lignes: ",i)
        
#e6

#s7
print("Albums d'artistes dont le nom débute par A")
i=0
for row in cursor.execute('''SELECT Title FROM Album WHERE ArtistId in ( 
                                 SELECT ArtistId FROM Artist WHERE Name LIKE 'A%'
                                 )'''):
    if i<10:
        print(row)
    i=i+1
print("Nombre total de lignes: ",i)
        
#e7

#s8
print("Albums et artistes ")
i=0
for row in cursor.execute("SELECT Album.Title, Artist.Name FROM Album, Artist WHERE Album.ArtistId=Artist.ArtistId"):
    if i<10:
        print(row)
    i=i+1
print("Nombre total de lignes: ",i)
        
#e8


#s9
i=0
for row in cursor.execute("SELECT Album.Title, Artist.Name FROM Album, Artist "):
    if i<10:
        print(row)
    i=i+1
print("Nombre total de lignes: ",i)
        
#e9


#s10

for row in cursor.execute("SELECT AlbumId, Title FROM Album ORDER BY Title ASC LIMIT 5"):
    print(row)

#e10 


#s11

for row in cursor.execute("SELECT TrackId, Name, Milliseconds FROM Track ORDER BY Milliseconds DESC, Name ASC LIMIT 5"):
    print(row)

#e11


#s12

for row in cursor.execute("SELECT Artist.Name, Album.Title FROM Album INNER JOIN Artist ON Artist.ArtistId = Album.ArtistId ORDER BY Artist.Name ASC LIMIT 5"):
    print(row)

#e12

#s13

for row in cursor.execute("SELECT Artist.Name, Album.Title FROM Artist LEFT JOIN Album ON Artist.ArtistId = Album.ArtistId WHERE Album.Title is NULL ORDER BY Name ASC LIMIT 5"):
    print(row)

#e13

print("14")
#s14

for row in cursor.execute("SELECT Album.Title, COUNT(Track.TrackId)  FROM Album INNER JOIN Track ON Album.AlbumId = Track.AlbumId GROUP BY Album.AlbumId ORDER BY COUNT(Track.TrackId) DESC LIMIT 5"):
    print(row)

#e14

print("15")
#s15

for row in cursor.execute("SELECT AlbumId, COUNT(TrackId)  FROM Track GROUP BY AlbumId LIMIT 5"):
    print(row)

#e15

print("16")
#s16

for row in cursor.execute("SELECT AlbumId, COUNT(TrackId)  FROM Track LIMIT 5"):
    print(row)

#e16

print("17")
#s17

for row in cursor.execute("SELECT AlbumId, Name, TrackId  FROM Track ORDER BY AlbumId ASC LIMIT 15"):
    print(row)

#e17


print("18")
#s18

for row in cursor.execute("SELECT ArtistId, group_concat(Title, ' !! ')  FROM Album GROUP BY ArtistId LIMIT 5"):
    print(row)

#e18






# Toujours fermer la connexion quand elle n'est plus utile
conn.close()
