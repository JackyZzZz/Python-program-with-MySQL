# insert_student.py

import mysql.connector

def insertStudent(UCINetID, email, first_name, middle_name, last_name, conn):
    cursor = conn.cursor()
    try:
        # Insert into the 'users' table
        user_insert_query = """
        INSERT INTO users (UCINetID, FirstName, MiddleName, LastName)
        VALUES (%s, %s, %s, %s)
        """
        # Handle the 'NULL' value for MiddleName
        middle_name_value = None if middle_name == 'NULL' else middle_name
        user_data = (UCINetID, first_name, middle_name_value, last_name)
        cursor.execute(user_insert_query, user_data)

        # Insert into the 'students' table
        student_insert_query = """
        INSERT INTO students (UCINetID)
        VALUES (%s)
        """
        cursor.execute(student_insert_query, (UCINetID,))

        # Insert into the 'emails' table
        email_insert_query = """
        INSERT INTO emails (UCINetID, Email)
        VALUES (%s, %s)
        """
        cursor.execute(email_insert_query, (UCINetID, email))

        conn.commit()
        return True

    except mysql.connector.Error as error:
        print(f"Error: {error}")
        conn.rollback()  # Rollback on any error
        return False

    finally:
        if cursor is not None:
            cursor.close()
