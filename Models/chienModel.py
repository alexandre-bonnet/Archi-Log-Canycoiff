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
    allDogIds = getAllDogIds(client_id)
    dogList = []
    for dogId in allDogIds:
        mycursor.execute("SELECT * FROM CHIEN WHERE id = %s",(dogId,))
        result = mycursor.fetchone()
        dogList.append({'id':dogId,'Nom':result["nom"],'Race':result["race"], 'Photo':result["photo"]})
    mycursor.close()
    mydb.close()
    return dogList


def isDogOwnedByClient(dog_id, client_id):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT id FROM CHIEN WHERE id = %s AND client_id = %s", (dog_id, client_id))
    result = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    return result is not None


def removeDog(pChien_id):
    mydb = connection.connect()
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM faire WHERE chien_id = %s", (pChien_id,))
    mycursor.execute("DELETE FROM CHIEN WHERE id = %s", (pChien_id,))
    mydb.commit()
    mycursor.close()
    mydb.close()
    return 200
