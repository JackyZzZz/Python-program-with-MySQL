import mysql.connector

def addEmail(UCINetID, email, conn):
    cursor = conn.cursor()
    try:
        # Add email to the 'emails' table for the user
        add_email_query = """
        INSERT INTO emails (UCINetID, Email)
        VALUES (%s, %s)
        """

        # Handle NULL values
        UCINetID_value = None if UCINetID == 'NULL' else UCINetID
        email_value = None if email == 'NULL' else email

        cursor.execute(add_email_query, (UCINetID_value, email_value))
        conn.commit()
        print('Success')
        return True

    except mysql.connector.Error as error:
        conn.rollback()
        print('Fail')
        return False

    finally:
        if cursor is not None:
            cursor.close()