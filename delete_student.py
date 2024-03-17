import mysql.connector

def deleteStudent(UCINetID, conn):
    cursor = conn.cursor()
    try:
        # Delete from the 'students' table
        delete_student_query = """
        DELETE FROM students
        WHERE UCINetID = %s
        """
        UCINetID_value = None if UCINetID == 'NULL' else UCINetID
        cursor.execute(delete_student_query, (UCINetID_value,))

        # Delete from the 'users' table
        delete_user_query = """
        DELETE FROM users
        WHERE UCINetID = %s
        """
        cursor.execute(delete_user_query, (UCINetID_value,))

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

