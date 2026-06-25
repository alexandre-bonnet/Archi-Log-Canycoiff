import mysql.connector 
import connection 

def addSortie(pDate_Sortie):
    mydb = connection.connect()
    mycursor = mydb.cursor()
    
    mycursor.execute("INSERT INTO sortie(date_sortie) VALUES (%s)",(pDate_Sortie,))
    mydb.commit()
    mycursor.close()
    mydb.close()
    return 203

def getSortieList(client_id):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)

    query = """
        SELECT DISTINCT s.id, s.date_sortie
        FROM sortie s
        JOIN faire f ON s.id = f.sortie_id
        JOIN chien c ON f.chien_id = c.id
        WHERE c.client_id = %s
        ORDER BY s.date_sortie ASC
    """

    mycursor.execute(query, (client_id,))
    results = mycursor.fetchall()

    sortieList = []
    for row in results:
        sortieList.append({
            "Id": row["id"],
            "Date": str(row["date_sortie"])
        })

    mycursor.close()
    mydb.close()

    return sortieList

def addDogToSortie(pChien_id,sortie_id):
    mydb = connection.connect()
    mycursor = mydb.cursor()
    mycursor.execute(
        "INSERT INTO faire(chien_id, sortie_id) VALUES (%s, %s)",(pChien_id, sortie_id))
    mydb.commit()
    mycursor.close()
    mydb.close()
    return 200

def getSortieId(pDate_Sortie):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM SORTIE WHERE date_sortie = %s",(pDate_Sortie,))
    result = mycursor.fetchone()
    if result is None:
        print("===========Sortie Don't Exist")
        mycursor.close()
        mydb.close()
        return None
    id = result["id"]
    mycursor.close()
    mydb.close()
    return id


def getDogsForSortie(client_id, sortie_id):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    query = """
        SELECT c.id, c.Nom, c.Race, c.Photo
        FROM chien c
        JOIN faire f ON c.id = f.chien_id
        WHERE f.sortie_id = %s AND c.client_id = %s
        ORDER BY c.Nom ASC
    """
    mycursor.execute(query, (sortie_id, client_id))
    results = mycursor.fetchall()
    dogList = []
    for row in results:
        dogList.append({
            'id': row['id'],
            'Nom': row['Nom'],
            'Race': row['Race'],
            'Photo': row['Photo']
        })
    mycursor.close()
    mydb.close()
    return dogList