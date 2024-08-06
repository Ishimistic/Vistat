
import mysql.connector as sql  # For connecting sql database and python program

from utils.dbConnection import connect_to_db

def displayCustomerDetails():
    mycon = connect_to_db()
    if mycon is None:
        print("Failed to connect to the database.")
        return
        
    mycur = mycon.cursor()
    mycur.execute("select * from customer_details")
    data = mycur.fetchall()
    for row in data:
        print(row)
    print("Total Records are-", mycur.rowcount)

    mycon.close()
    

def displayOrderDetails():
    mycon = connect_to_db()
    if mycon is None:
        print("Failed to connect to the database.")
        return
    
    mycur = mycon.cursor()
    mycur.execute("select * from order_details")
    data = mycur.fetchall()
    for row in data:
        print(row)
    print("Total Records are-", mycur.rowcount)

    mycon.close()


def displayServiceDetails():
    mycon = connect_to_db()
    if mycon is None:
        print("Failed to connect to the database.")
        return
    
    mycur = mycon.cursor()
    mycur.execute("select * from services")
    data = mycur.fetchall()
    for row in data:
        print(row)
    print("Total Records are-", mycur.rowcount)

    mycon.close()


