import mysql.connector
from constants import Constants

def connect():
    """
    Connect to the database
    """

    try:
        db_connection = mysql.connector.connect(user=Constants.USER, password=Constants.PASSWORD, database = Constants.DATABASE)
        return db_connection
    except mysql.connector.Error as error:
        pass

def initialize_database():
    """
    Initialize the database schema
    """

    sql_file_path = 'cs122a_db.sql'

    try:
        db_connection = mysql.connector.connect(user=Constants.USER, password=Constants.PASSWORD)

        cursor = db_connection.cursor()
        # Open and read the SQL file
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        # Execute each statement in the SQL file
        for statement in sql_script.split(';'):
            # Ignore empty statements (which can occur due to splitting by ';')
            if statement.strip():
                # print("running: ", statement)
                cursor.execute(statement)

        db_connection.commit()

    except mysql.connector.Error as error:
        pass

    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()