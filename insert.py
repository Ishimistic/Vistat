import mysql.connector as sql;
from utils.dbConnection import connect_to_db;

def insertDetailsInCustomer():
    
    mycon = connect_to_db()
    if not mycon:
        return
    
    try: 
        mycur = mycon.cursor()
        
        # Get input from user
        Name = input("Enter Name: ")
        Phone_No = input("Enter Phone No.: ")
        VIN = input("Enter VIN: ")
        model = input("Enter Model: ")
        variant = input("Enter Variant: ")
        mode_of_payment = input("Enter Mode of Payment: ")
        email_id = input("Enter Email-ID: ")
        Address = input("Enter Address: ")
        date_of_purchase = input("Enter Date of Purchase: ")
        
        # Insert data into database
        query = "INSERT INTO order_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (Name, Phone_No, VIN, model, variant, mode_of_payment, email_id, Address)
        
        mycur.execute(query, data)
        mycon.commit()
        
        print("Record Added Successfully")
        
    except sql.Error as e:
        print(f"Error inserting record: {e}")
    
    finally:
        if mycon and mycon.is_connected():
            mycon.close()


def insertDetailsInOrder():  # Inserting Records in order Details
    mycon = connect_to_db()
    if not mycon:
        return
    
    try: 
        mycur = mycon.cursor() 
        
        VIN = input("Enter VIN: ")
        Phone_No = input("Enter Phone No.: ")
        Model = input("Enter Model: ")
        Varient = input("Enter Varient: ")
        Date_of_Purchase = input("Enter Date of Purchase: ")
        Date_of_Delivery = input("Enter Date of Delivery: ")
        Delivery_Address = input("Enter Delivery Address: ")
        Ex_Showroom_Price = input("Enter Ex Showroom Price: ")
        
        if VIN and Phone_No and Model and Varient and Date_of_Purchase and Date_of_Delivery and Delivery_Address and Ex_Showroom_Price:
            query2 = """
                INSERT INTO order_details (VIN, Phone_No, Model, Varient, Date_of_Purchase, Date_of_Delivery, Delivery_Address, Ex_Showroom_Price)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (VIN, Phone_No, Model, Varient, Date_of_Purchase, Date_of_Delivery, Delivery_Address, Ex_Showroom_Price)
            mycur.execute(query2, data)
            mycon.commit()
            print("Record Added")
        else:
            print("All fields are required.")
        
    except sql.Error as e:
        print(f"Error: {e}")
    
    finally:
        if mycon.is_connected():
            mycon.close()

def insertDetailsInServices():  # Inserting Records in services
    mycon = connect_to_db()
    if not mycon:
        return
    
    try: 
        mycur = mycon.cursor()
        
        VIN = input("Enter VIN: ")
        Free_services = input("Enter Free Services: ")
        KM = input("Enter KM: ")
        
        if VIN and Free_services and KM:
            query3 = """
                INSERT INTO services (Free_services, KM, VIN)
                VALUES (%s, %s, %s)
            """
            data = (Free_services, KM, VIN)
            mycur.execute(query3, data)
            mycon.commit()
            print("Record Added")
        else:
            print("All fields are required.")
        
    except sql.Error as e:
        print(f"Error: {e}")
    
    finally:
        if mycon.is_connected():
            mycon.close()
