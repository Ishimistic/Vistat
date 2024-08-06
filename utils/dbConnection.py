import mysql.connector as sql;

def connect_to_db():
    try:
        mycon = sql.connect(
            host="localhost", user="root", passwd="tintin1234", database="vistat"
        )
        if not mycon.is_connected():
            raise Exception("Error in connection")
        return mycon
    except sql.Error as e:
        print(f"Error: {e}")
        return None
