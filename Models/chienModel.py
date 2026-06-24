import mysql.connector 
import connection 

def addChien(pNom, pRace,pClient_id):
    db = connexion.connect()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO chien(nom, race, client_id) VALUES (%s, %s, %s)",
        (pNom, pRace, pClient_id))

    db.commit()
    cursor.close()
    db.close()
    return 


def addSortie(pDate_Sortie, pChien_id):
    db = connexion.connect()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO sortie(date_sortie, chien_id) VALUES (%s, %s)",
        (pDate_Sortie, pChien_id))


    db.commit()
    cursor.close()
    db.close()
    return 




  

   
