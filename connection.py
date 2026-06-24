import mysql.connector 

def connect():
    try :
        mydb = mysql.connector.connect(
            host="localhost",
            user="roro",
            password="r0r0",
            database="canycoiff"
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return mydb 