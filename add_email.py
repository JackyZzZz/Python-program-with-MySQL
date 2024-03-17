# add_email.py

import mysql.connector

def addEmail(UCINetID, email, conn):
    cursor = conn.cursor()
    try:
        # Add email to the 'emails' table for the user
        add_email_query = """
        INSERT INTO emails (UCINetID, Email)
        VALUES (%s, %s)
        """
        cursor.execute(add_email_query, (UCINetID, email))
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