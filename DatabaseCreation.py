import mysql.connector 

host='localhost'
user='root'
password='root'
database='LLADADDB'

def createDB():
    mycon = mysql.connector.connect(host=host, user=user, password=password)    #connection(host, user, password)
    mycursor = mycon.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS LLADADDB")
    mycursor.execute("SHOW DATABASES")

    mycon.close()
    # To see the database instance print 

    # for x in mycursor:
    #     print(x)

# createDB()

def createTables():
    mycon = mysql.connector.connect(host=host, user=user, password=password, database=database)

    mycursor = mycon.cursor()

    # creating LLADB table 
    LLADB_Query = "CREATE TABLE IF NOT EXISTS LLADB(ID int NOT NULL AUTO_INCREMENT, NS_ADDRESS VARCHAR(255),    PRIMARY KEY (ID))"
    mycursor.execute(LLADB_Query)

    # creating DADDB table 
    DADDB_Query = "CREATE TABLE IF NOT EXISTS DADDB(ID int NOT NULL AUTO_INCREMENT, NA_ADDRESS VARCHAR(255),    PRIMARY KEY (ID))"
    mycursor.execute(DADDB_Query)

    print("Database Initializing Complete")
    mycon.close()
    
def init():
    print("Initializing Database")
    createDB()
    createTables()


init()

