import mysql.connector
import connection 

mydb = connection.connect()
mycursor = mydb.cursor(dictionary=True)



mycursor.execute("CREATE DATABASE IF NOT EXISTS canycoiff") #on cree la bdd
mycursor.execute("USE canycoiff")

#on crée la table CLIENT 
mycursor.execute("""CREATE TABLE IF NOT EXISTS client (   
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50),
    telephone VARCHAR(50))""")

#table users (relié client)
mycursor.execute( """
   CREATE TABLE IF NOT EXISTS `USER` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    client_id INT,
    FOREIGN KEY (client_id) REFERENCES CLIENT(id)
    );
   """
)

#la table CHIEN (chaque chien appartient a un client)
mycursor.execute("""CREATE TABLE IF NOT EXISTS chien (  
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50),
    race VARCHAR(50),
    photo VARCHAR(50),
    client_id INT,
    FOREIGN KEY (client_id) REFERENCES client(id))""") #clé étrangère de client

#la table sortie 
mycursor.execute("""
CREATE TABLE IF NOT EXISTS sortie (id INT AUTO_INCREMENT PRIMARY KEY,date_sortie DATE)""")
quit

#table de liaison "faire" car un chien peut faire plusieurs sorties et une sortie peut etre faite par plusieurs chiens (relation N-N)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS faire (
    chien_id INT,
    sortie_id INT,
    PRIMARY KEY (chien_id, sortie_id),
    FOREIGN KEY (chien_id) REFERENCES chien(id), 
    FOREIGN KEY (sortie_id) REFERENCES sortie(id))""") 

#On ajoute clients+chiens: 
while True:
    nom_client = input("\nNom du client (q pour quitter) : ")
    if nom_client == "q":
        break
    telephone = input("Téléphone : ")

    # on ajoute le client 
    sql = "INSERT INTO client (nom, telephone) VALUES (%s, %s)"
    mycursor.execute(sql, (nom_client, telephone))
    mydb.commit()
    #on recupere l'id du client
    client_id = mycursor.lastrowid
    print("Client ajouté, youpi !")

 #ajout chien 
    while True:
        nom_chien = input("Nom du chien (q pour terminer les chiens) : ")
        if nom_chien == "q":
            break
        race = input("Race : ")
        client_id = input("Id du client(q pour terminer) : ")
        sql = """INSERT INTO chien (nom, race, client_id) VALUES (%s, %s, %s)"""
        mycursor.execute(sql,(nom_chien, race, client_id))
        mydb.commit()
        print("Toutou ajouté!")


#on ajoute les sorties: 
while True:
    date_sortie = input(
        "\nDate de sortie AAAAA-MM-JJ (q pour quitter) : ")
    if date_sortie == "q":
        break

# on crée la sortie 
    mycursor.execute("INSERT INTO sortie (date_sortie) VALUES (%s)",(date_sortie,))
    mydb.commit()
    sortie_id = mycursor.lastrowid #id de sortie 
    print("\nListe des chiens :")

    mycursor.execute("SELECT id, nom FROM chien")
    for chien in mycursor.fetchall():
        print(chien)

    print("\nEntrez les ids des chiens participant à la sortie.")

    while True:

        id_chien = input("Id du chien (q pour terminer) : ")
        if id_chien == "q":
            break

        mycursor.execute("""INSERT INTO faire(chien_id, sortie_id) VALUES (%s, %s)""",(id_chien, sortie_id))
        mydb.commit()


#au final: 
print("\nSorties")

mycursor.execute("""SELECT
sortie.date_sortie,
    chien.nom
FROM faire
JOIN chien
    ON faire.chien_id = chien.id
JOIN sortie
    ON faire.sortie_id = sortie.id
ORDER BY sortie.date_sortie
""")

for ligne in mycursor.fetchall():
    print(ligne)

mycursor.close() 
