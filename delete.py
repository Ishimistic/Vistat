import mysql.connector as sql;
from utils.dbConnection import connect_to_db;
from utils.thankYou import thankyou;

def deleteFromCustomer():
    mycon = connect_to_db()
    if mycon is None:
        print("Failed to connect to the database.")
        return
    
    try:    
        mycur = mycon.cursor()
        VIN = input("Enter VIN: ")

        mycur.execute("SELECT * FROM customer_details WHERE VIN = %s", (VIN,))
        data = mycur.fetchall()
        
        if not data:
            print(f"No records found for VIN: {VIN}")
            return

        for row in data:
            print(row)
        
        c = input("Do you want to delete this record? (y/n): ")
        if c.lower() == 'y':
            mycur.execute("DELETE FROM customer_details WHERE VIN = %s", (VIN,))
            mycon.commit()
            print("Record deleted.")
            
            print("Records in table after deletion:")
            mycur.execute("SELECT * FROM customer_details")
            data = mycur.fetchall()
            for row in data:
                print(row)
            thankyou()  

    except sql.Error as e:
        print(f"Error: {e}")
    
    finally:
        if mycon.is_connected():
            mycon.close()


def deleteFromOrder():
    try:
        mycon = sql.connect(
            host="localhost", user="root", passwd="tintin1234", database="vistat"
        )
        
        if not mycon.is_connected():
            print("Error in connection")
            return
        
        mycur = mycon.cursor()
        VIN = input("Enter VIN: ")

        mycur.execute("SELECT * FROM order_details WHERE VIN = %s", (VIN,))
        data = mycur.fetchall()
        
        if not data:
            print(f"No records found for VIN: {VIN}")
            return

        for row in data:
            print(row)
        
        c = input("Do you want to delete this record? (y/n): ")
        if c.lower() == 'y':
            mycur.execute("DELETE FROM order_details WHERE VIN = %s", (VIN,))
            mycon.commit()
            print("Record deleted.")
            
            print("Records in table after deletion:")
            mycur.execute("SELECT * FROM order_details")
            data = mycur.fetchall()
            for row in data:
                print(row)

    except sql.Error as e:
        print(f"Error: {e}")
    
    finally:
        if mycon.is_connected():
            mycon.close()


def deleteFromService():
    try:
        mycon = sql.connect(
            host="localhost", user="root", passwd="tintin1234", database="vistat"
        )
        
        if not mycon.is_connected():
            print("Error in connection")
            return
        
        mycur = mycon.cursor()
        VIN = input("Enter VIN: ")

        mycur.execute("SELECT * FROM services WHERE VIN = %s", (VIN,))
        data = mycur.fetchall()
        
        if not data:
            print(f"No records found for VIN: {VIN}")
            return

        for row in data:
            print(row)
        
        c = input("Do you want to delete this record? (y/n): ")
        if c.lower() == 'y':
            mycur.execute("DELETE FROM services WHERE VIN = %s", (VIN,))
            mycon.commit()
            print("Record deleted.")
            
            print("Records in table after deletion:")
            mycur.execute("SELECT * FROM services")
            data = mycur.fetchall()
            for row in data:
                print(row)
        
    except sql.Error as e:
        print(f"Error: {e}")
    
    finally:
        if mycon.is_connected():
            mycon.close()

