import mysql.connector
import connection

def getUserCount(pUsername):
    mycursor = connection.connect()
    mycursor.execute("SELECT COUNT(*) FROM USER WHERE username = %s",(pUsername,))
    result = mycursor.fetchone()
    count = result[0]
    mycursor.close()
    return count


def addUser(pUsername,pPassword):
    mycursor = connection.connect()
    mycursor.execute('''insert into USER VALUES (null,%s,%s)''',(pUsername,pPassword))
    print("user added")
    mycursor.close()
    return True