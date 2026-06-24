import mysql.connector 
import connection 

def getChienCount(pAddDog):
    db = connexion.connect()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO chien(nom, race, client_id) VALUES (%s, %s, %s)",
        (nom, race, client_id)
    )
    cursor.execute(
        "INSERT INTO sortie(date_sortie, chien_id) VALUES (%s, %s)",
        (date_sortie, chien_id)
    )


    db.commit()
    cursor.close()
    db.close()
    return getChienCount




  

   
