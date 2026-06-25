import mysql.connector 
import connection 

def addChien(pNom, pRace,pClient_id, pPhoto):
    mydb = connection.connect()
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO chien(nom, race, client_id, photo) VALUES (%s, %s, %s, %s)",(pNom, pRace, pClient_id, pPhoto))

    mydb.commit()
    mycursor.close()
    mydb.close()
    return 

def getDogName(dog_id):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT nom FROM CHIEN WHERE id = %s",(dog_id,))
    result = mycursor.fetchone()
    name = result["nom"]
    mycursor.close()
    return name

def getDogRace(dog_id):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT race FROM CHIEN WHERE id = %s",(dog_id,))
    result = mycursor.fetchone()
    race = result["race"]
    mycursor.close()
    return race

def getAllDogIds(client_id):
    allDogIds =[]
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute('''SELECT id FROM CHIEN WHERE client_id = %s''',(client_id,))
    for chien in mycursor:
        allDogIds.append(chien["id"])
    mycursor.close()
    mydb.close()
    return allDogIds

def getDogList(client_id):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute(
        "SELECT nom, race, photo FROM CHIEN WHERE client_id = %s",
        (client_id,)
    )

    dogList = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return dogList




  

   
