# insert_use.py

import mysql.connector

def insertUse(projectId, studentUCINetID, machineId, start_date, end_date, conn):
    """
    Insert a new use record into the database
    """

    cursor = conn.cursor()
    try:
        query = "INSERT INTO StudentUseMachinesInProject VALUES (%s, %s, %s, %s, %s)"

        # Handle NULL values
        projectId_values = None if projectId == "NULL" else projectId
        studentUCINetID_values = None if studentUCINetID == "NULL" else studentUCINetID
        machineId_values = None if machineId == "NULL" else machineId
        start_date_values = None if start_date == "NULL" else start_date
        end_date_values = None if end_date == "NULL" else end_date

        cursor.execute(query, (projectId_values, studentUCINetID_values, machineId_values, start_date_values, end_date_values))
        conn.commit()
        print('Success')
    except mysql.connector.Error as error:
        conn.rollback()
        print('Fail')

    finally:
        cursor.close()
