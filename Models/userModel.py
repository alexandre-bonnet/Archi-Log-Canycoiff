import mysql.connector
import connection

def getUserCount(pUsername):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT COUNT(*) as total FROM USER WHERE username = %s",(pUsername,))
    result = mycursor.fetchone()
    count = result["total"]
    print("===============")
    print(count)
    print("===============")
    mycursor.close()
    return count


def addUser(pUsername,pPassword):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute('''insert into USER VALUES (null,%s,%s)''',(pUsername,pPassword))
    print("user added")
    mycursor.close()
    return True

def passwordValidity(pUsername,pPassword):
    mydb = connection.connect()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute('''SELECT password from USER where username = %s''',(pUsername,))
    result = mycursor.fetchone()
    password = result["password"]
    print("=========== PWD")
    print(password)
    mycursor.close()
    if(password == pPassword):
        return True
    return False