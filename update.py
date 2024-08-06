import mysql.connector as sql
from utils.dbConnection import connect_to_db;


def updateCustomer():
    mycon = connect_to_db()
    if mycon is None:
        print("Failed to connect to the database.")
        return
    
    try:
        mycur = mycon.cursor()
        VIN = input("Enter registered VIN: ")
        
        print("SUBMENU")
        print("1. Update Name")
        print("2. Update Phone No.")
        print("3. Update VIN")
        print("4. Update Model")
        print("5. Update Variant")
        print("6. Update Mode of Payment")
        print("7. Update Email ID")
        print("8. Update Address")
        print("9. Update Date Of Purchase")
        
        choice = input("Choose the option to change respective values: ")
        
        updates = {
            "1": "Name",
            "2": "Phone_No",
            "3": "VIN",
            "4": "Model",
            "5": "Variant",
            "6": "Mode_of_Payment",
            "7": "Email_ID",
            "8": "Address",
            "9": "Date_of_Purchase"
        }
        
        if choice in updates:
            new_value = input(f"Enter updated {updates[choice]}: ")
            mycur.execute(
                f"UPDATE customer_details SET {updates[choice]} = %s WHERE VIN = %s",
                (new_value, VIN)
            )
            print("Your record is updated.")
        else:
            print("Wrong choice")
        
        mycur.execute("SELECT * FROM customer_details")
        data = mycur.fetchall()
        for row in data:
            print(row)
        
        mycon.commit()
        
    except sql.Error as e:
        print(f"Error: {e}")
    
    finally:
        if mycon.is_connected():
            mycon.close()

def updateOrder():
    mycon = connect_to_db()
    if mycon is None:
        print("Failed to connect to the database.")
        return
    
    try:
        mycur = mycon.cursor()
        VIN = input("Enter registered VIN: ")
        
        print("SUBMENU")
        print("1. Update VIN")
        print("2. Update Phone No.")
        print("3. Update Model")
        print("4. Update Variant")
        print("5. Update Date of Purchase")
        print("6. Update Date of Delivery")
        print("7. Update Delivery Address")
        print("8. Update Ex Showroom Price")
        
        choice = int(input("Choose the option to change respective values: "))
        
        updates = {
            1: "VIN",
            2: "Phone_No",
            3: "Model",
            4: "Variant",
            5: "Date_of_Purchase",
            6: "Date_of_Delivery",
            7: "Delivery_Address",
            8: "Ex_Showroom_Price"
        }
        
        if choice in updates:
            new_value = input(f"Enter updated {updates[choice]}: ")
            mycur.execute(
                f"UPDATE order_details SET {updates[choice]} = %s WHERE VIN = %s",
                (new_value, VIN)
            )
            print("Your record is updated.")
        else:
            print("Wrong choice")
        
        mycur.execute("SELECT * FROM order_details")
        data = mycur.fetchall()
        for row in data:
            print(row)
        
        mycon.commit()
        
    except sql.Error as e:
        print(f"Error: {e}")
    
    finally:
        if mycon.is_connected():
            mycon.close()

def updateService():
    mycon = connect_to_db()
    if mycon is None:
        print("Failed to connect to the database.")
        return
    
    try:
        mycur = mycon.cursor()
        VIN = input("Enter registered VIN: ")
        
        print("SUBMENU")
        print("1. Update No. of free services")
        print("2. Update K.M. for Services")
        print("3. Update VIN")
        
        choice = int(input("Choose the option to change respective values: "))
        
        updates = {
            1: "no_of_free_services",
            2: "KM_for_services",
            3: "VIN"
        }
        
        if choice in updates:
            new_value = input(f"Enter updated {updates[choice]}: ")
            mycur.execute(
                f"UPDATE services SET {updates[choice]} = %s WHERE VIN = %s",
                (new_value, VIN)
            )
            print("Your record is updated.")
        else:
            print("Wrong choice")
        
        mycur.execute("SELECT * FROM services")
        data = mycur.fetchall()
        for row in data:
            print(row)
        
        mycon.commit()
        
    except sql.Error as e:
        print(f"Error: {e}")
    
    finally:
        if mycon.is_connected():
            mycon.close()

