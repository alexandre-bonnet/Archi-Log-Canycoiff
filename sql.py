import mysql.connector 
import connection


mydb = connection.connect()


mycursor = mydb.cursor()

mycursor.execute( """
   CREATE TABLE IF NOT EXISTS CHIEN(chien_id int auto_increment primary key, nom VARCHAR(50), race_id int)
   """
)
mycursor.execute( """
   CREATE TABLE IF NOT EXISTS USER(id int auto_increment primary key, username VARCHAR(50), password VARCHAR(50))
   """
)
mycursor.execute( """
   CREATE TABLE IF NOT EXISTS RACE(race_id int auto_increment primary key, nom_race VARCHAR(50))
   """
)


def resetTableRace():
    races = ["Berger-allemand","Jack-russle","Poodle"]
    mycursor.execute("DELETE from RACE")
    for race in races:
        mycursor.execute("INSERT INTO RACE (nom_race) VALUES (%s)", (race,))
        mydb.commit()

def resetTableUser():
    mycursor.execute("DELETE from USER")
    mycursor.execute('''insert into USER VALUES
                 (null,'RomaneJouvet3','1234'),
                 (null,'AlexB','qsdfghjklm')''')
    
    mydb.commit()

resetTableUser()

mycursor.execute("SELECT * FROM RACE")
for row in mycursor.fetchall():
    print(row)
print("=========================")
mycursor.execute("SELECT * FROM USER")
for row in mycursor.fetchall():
    print(row)

mycursor.close()
mydb.close()