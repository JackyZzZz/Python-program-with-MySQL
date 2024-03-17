#adminEmails.py

import mysql.connector

def adminEmails(machineId, conn):
    """
    Given a machine ID, find all administrators of that machine.
    List the emails of those administrators. Ordered by netid ascending.
    """

    cursor = conn.cursor()

    try:
        query = """
        SELECT 
            U.UCINetID, 
            U.FirstName, 
            U.MiddleName, 
            U.LastName, 
            GROUP_CONCAT(E.Email SEPARATOR ';') AS Emails
        FROM admins A
        JOIN manage M ON M.AdministratorUCINetID = A.UCINetID
        JOIN users U ON U.UCINetID = A.UCINetID
        JOIN emails E ON E.UCINetID = A.UCINetID
        WHERE M.MachineID = %s
        GROUP BY U.UCINetID
        ORDER BY U.UCINetID ASC
        """

        cursor.execute(query, (machineId,))
        result = cursor.fetchall()
        for row in result:
            print(','.join([str(item) if item else 'NULL' for item in row]))

    except mysql.connector.Error as error:
        pass

    finally:
        cursor.close()