import mysql.connector as sql;
from utils.dbConnection import connect_to_db;


# def searchRecInCustomer():
#     try:
#         mycon = sql.connect(
#             host="localhost", user="root", passwd="tintin1234", database="vistat"
#         )

#         if not mycon.is_connected():
#             print("Error in connection")
#             return

#         mycur = mycon.cursor()
#         VIN = input("Enter VIN: ")
#         mycur.execute("SELECT * FROM customer_details WHERE VIN = %s", (VIN,))
#         data = mycur.fetchall()
        
#         if data:
#             for row in data:
#                 print(row)
#         else:
#             print("No records found for VIN:", VIN)

#     except sql.Error as e:
#         print(f"Error: {e}")

#     finally:
#         if mycon.is_connected():
#             mycon.close()


def searchRecInOrder():
    mycon = connect_to_db()
    if mycon is None:
        print("Failed to connect to the database.")
        return
    
    try:
        mycur = mycon.cursor()
        VIN = input("Enter VIN: ")
        mycur.execute("SELECT * FROM order_details WHERE VIN = %s", (VIN,))
        data = mycur.fetchall()

        if data:
            for row in data:
                print(row)
        else:
            print("No records found for VIN:", VIN)

    except sql.Error as e:
        print(f"Error: {e}")

    finally:
        if mycon.is_connected():
            mycon.close()

def searchrecInServices():
    mycon = connect_to_db()
    if mycon is None:
        print("Failed to connect to the database.")
        return
    
    try:
        mycur = mycon.cursor()
        VIN = input("Enter VIN: ")
        mycur.execute("SELECT * FROM services WHERE VIN = %s", (VIN,))
        data = mycur.fetchall()

        if data:
            for row in data:
                print(row)
        else:
            print("No records found for VIN:", VIN)

    except sql.Error as e:
        print(f"Error: {e}")

    finally:
        if mycon.is_connected():
            mycon.close()

def search_records(table_name):
    mycon = connect_to_db()
    if mycon is None:
        print("Failed to connect to the database.")
        return
    
    try:
        mycur = mycon.cursor()
        VIN = input("Enter VIN: ")
        query = f"SELECT * FROM {table_name} WHERE VIN = %s"
        mycur.execute(query, (VIN,))
        data = mycur.fetchall()

        if data:
            for row in data:
                print(row)
        else:
            print(f"No records found for VIN: {VIN}")

    except sql.Error as e:
        print(f"Error: {e}")

    finally:
        if mycon.is_connected():
            mycon.close()

def searchRecInCustomer():
    search_records("customer_details")

def searchRecInOrder():
    search_records("order_details")

def searchrecInServices():
    search_records("services")
