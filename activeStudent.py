import mysql.connector

def activeStudent(machineId, N, startDate, endDate, conn):
    """
    Given a machine Id, find all active students that used it more than N times (including N)
    in a specific time range (including start and end date). Ordered by netid ascending.
    N will be at least 1.
    """

    cursor = conn.cursor()

    try:
        query = """
        SELECT U.UCINetID, U.FirstName, U.MiddleName, U.LastName
        FROM StudentUseMachinesInProject SUMIP
        JOIN users U ON U.UCINetID = SUMIP.StudentUCINetID
        WHERE SUMIP.MachineID = %s AND SUMIP.StartDate >= %s AND SUMIP.EndDate <= %s
        GROUP BY SUMIP.StudentUCINetID
        HAVING COUNT(*) >= %s
        ORDER BY U.UCINetID ASC
        """

        cursor.execute(query, (machineId, startDate, endDate, N))
        result = cursor.fetchall()
        for row in result:
            print(','.join([str(item) if item else 'NULL' for item in row]))
    except mysql.connector.Error as error:
        pass

    finally:
        cursor.close()