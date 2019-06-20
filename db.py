import mysql.connector 

# Create a connection object

host='localhost'
user='root'
password='root'
database='LLADADDB'

def connection(host, user, password, database=None):
    if database is None:
        # print("1")
        myConnection = mysql.connector.connect(host=host, user=user, password=password)
    else:
        # print("2")
        myConnection = mysql.connector.connect(host=host, user=user, password=password, database=database)

    return myConnection
  
def createDB():
    mycon = connection(host, user, password) #mysql.connector.connect(host=host, user=user, password=password)    #connection(host, user, password)
    mycursor = mycon.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS LLADADDB")
    mycursor.execute("SHOW DATABASES")

    print(" Created Database ")

    mycon.close()
    # To see the database instance print 

    # for x in mycursor:
    #     print(x)

def createTables():
    """
    try:
        mycon = connection(host, user, password, database)
    except Exception:
        print("Error in MySQL connexion")

    mycon = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="mydatabase"
    )
    """
    mycon = connection(host, user, password, database)

    mycursor = mycon.cursor()

    # creating LLADB table 
    LLADB_Query = "CREATE TABLE IF NOT EXISTS LLADB(ID int NOT NULL AUTO_INCREMENT, NS_ADDRESS VARCHAR(255),    PRIMARY KEY (ID))"
    mycursor.execute(LLADB_Query)

    # creating DADDB table 
    DADDB_Query = "CREATE TABLE IF NOT EXISTS DADDB(ID int NOT NULL AUTO_INCREMENT, NA_ADDRESS VARCHAR(255),    PRIMARY KEY (ID))"
    mycursor.execute(DADDB_Query)

    mycon.close()

    print("Tables Created")


def insertDataInLLADB(val):
    mycon = connection(host, user, password, database)
    
    mycursor = mycon.cursor()
    # val = "fe80::6c91:28fd:3971:3e87"

    sql = "INSERT INTO LLADB SET NS_ADDRESS = '" + val + "'" 
    mycursor.execute(sql)

    mycon.commit()

    print(mycursor.rowcount, "record inserted.")

    mycon.close()

def insertDataInDADDB(val):
    mycon = connection(host, user, password, database)
    
    mycursor = mycon.cursor()
    # val = "fe80::6c91:28fd:3971:3e87"

    sql = "INSERT INTO DADDB SET NA_ADDRESS = '" + val + "'" 
    mycursor.execute(sql)

    mycon.commit()

    mycon.close()
    print(mycursor.rowcount, "record inserted.")

def fetchDataFromLLADB(val):
    mycon = connection(host, user, password, database)
    
    mycursor = mycon.cursor()

    sql = "SELECT NS_ADDRESS FROM  LLADB WHERE NS_ADDRESS = '" + val + "'"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    print(sql)
    print("Successful ", myresult)

    mycon.close()
    return myresult
    # print(myresult)
    # for x in myresult:
    #     print(x)

def fetchDataFromDADDB(val):
    mycon = connection(host, user, password, database)

    mycursor = mycon.cursor()

    sql = "SELECT NA_ADDRESS FROM  DADDB WHERE NA_ADDRESS = '" + val + "'"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    print(sql)
    print("Successful ", myresult)

    mycon.close()
    return myresult
    # print(myresult)
    # for x in myresult:
    #     print(x)

def truncateTAbles():
    mycon = connection(host, user, password, database)
    mycursor = mycon.cursor()

    sql = "TRUNCATE LLADB"
    sql2 = "TRUNCATE DADDB"
    mycursor.execute(sql)
    mycursor.execute(sql2)
    print("Flushing database table")

    mycon.close()

# createDB()
# createTables()
# fetchDataFromLLADB("fe80::6c91:28fd:3971:3e87")
# insertDataInDADDB("fe80::6c91:28fd:3971:3e87")
# insertDataInLLADB("fe80::6c91:28fd:3971:3e87")





