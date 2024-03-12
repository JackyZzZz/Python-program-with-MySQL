import mysql.connector

def insertUse(projectId, studentUCINetID, machineId, start_date, end_date, conn):
    """
    Insert a new use record into the database
    """

    cursor = conn.cursor()
    try:
        query = "INSERT INTO StudentUseMachinesInProject VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (projectId, studentUCINetID, machineId, start_date, end_date))
        conn.commit()
        print('Success')
    except mysql.connector.Error as error:
        conn.rollback()
        print('Fail')

    finally:
        cursor.close()
