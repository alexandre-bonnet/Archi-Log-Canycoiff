import mysql.connector
import connection


mydb = connection.connect()
mycursor = mydb.cursor()


def userValid(pUsername,pPassword):
    mydb = connection.connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT COUNT(*) FROM USER WHERE username = %s",(pUsername,))
    result = mycursor.fetchone()
    count = result[0]
    print(count)
    if(count>0):
        print("error ; username already exists")
        mycursor.close()
        mydb.close()
        return 400
    mycursor.close()
    mydb.close()
    return 200

def addUser(pUsername,pPassword):
    mydb = connection.connect()
    mycursor = mydb.cursor()
    mycursor.execute('''insert into USER VALUES (null,%s,%s)''',(pUsername,pPassword))
    mydb.commit()
    print("user added")
    mycursor.close()
    mydb.close()
    return 201

mycursor.close()
mydb.close()