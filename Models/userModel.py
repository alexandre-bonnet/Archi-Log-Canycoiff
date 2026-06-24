import mysql.connector
import connection

def getUserCount(pUsername):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT COUNT(*) as total FROM USER WHERE username = %s",(pUsername,))
    result = mycursor.fetchone()
    count = result["total"]
    mycursor.close()
    return count

def getUserId(pUsername):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT id FROM USER WHERE username = %s",(pUsername,))
    result = mycursor.fetchone()
    id = result["id"]
    mycursor.close()
    return id

def getUsername(user_id):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT username FROM USER WHERE id = %s",(user_id,))
    result = mycursor.fetchone()
    name = result["username"]
    mycursor.close()
    return name

def getClientId(user_id):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute('''SELECT client_id FROM USER u 
                     JOIN CLIENT c ON u.client_id = c.id WHERE u.id = %s''',(user_id,))
    result = mycursor.fetchone()
    if result is None:
        return None
    client_id = result["client_id"]
    mycursor.close()
    return client_id

def addUser(pUsername,pPassword):
    mydb = connection.connect()
    mycursor = mydb.cursor()
    mycursor.execute('''insert into USER VALUES (null,%s,%s,null)''',(pUsername,pPassword))
    mydb.commit()
    print("user added")
    mycursor.close()
    return True

def addClient(user_id,pName,pNumber):
    mydb = connection.connect()
    mycursor = mydb.cursor()
    mycursor.execute('''insert into CLIENT VALUES (null,%s,%s)''',(pName,pNumber))
    client_id = mycursor.lastrowid
    mycursor.execute("UPDATE USER SET client_id = %s WHERE id = %s",(client_id, user_id))
    mydb.commit()
    print("user added")
    mycursor.close()
    return True

def passwordValidity(pUsername,pPassword):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute('''SELECT password from USER where username = %s''',(pUsername,))
    result = mycursor.fetchone()
    password = result["password"]
    mycursor.close()
    if(password == pPassword):
        return True
    return False