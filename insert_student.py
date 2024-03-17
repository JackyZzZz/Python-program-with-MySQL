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
        # Handle the 'NULL' values
        UCINetID_value = None if UCINetID == 'NULL' else UCINetID
        first_name_value = None if first_name == 'NULL' else first_name
        middle_name_value = None if middle_name == 'NULL' else middle_name
        last_name_value = None if last_name == 'NULL' else last_name
        user_data = (UCINetID_value, first_name_value, middle_name_value, last_name_value)
        cursor.execute(user_insert_query, user_data)

        # Insert into the 'students' table
        student_insert_query = """
        INSERT INTO students (UCINetID)
        VALUES (%s)
        """
        cursor.execute(student_insert_query, (UCINetID_value,))

        # Insert into the 'emails' table
        email_insert_query = """
        INSERT INTO emails (UCINetID, Email)
        VALUES (%s, %s)
        """
        email_value = None if email == 'NULL' else email
        cursor.execute(email_insert_query, (UCINetID_value, email_value))

        conn.commit()
        return True

    except mysql.connector.Error as error:
        conn.rollback()
        return False

    finally:
        if cursor is not None:
            cursor.close()
