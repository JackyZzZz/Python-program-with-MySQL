import mysql.connector

def machineUsage(courseId, conn):
    """
    Given a course id, count the number of usage of each machine in that course.
    Each unique record in the MachineUse table counts as one usage.
    Machines that are not used in the course should have a count of 0 instead of NULL.
    Ordered by machineId descending.
    """

    cursor = conn.cursor()
    try:
        query = """
        SELECT 
        M.MachineID, 
        M.Hostname, 
        M.IPAddress, 
        COALESCE(SUM(CASE WHEN P.CourseID = %s THEN 1 ELSE 0 END), 0) AS UsageCount
        FROM machines M
        LEFT JOIN StudentUseMachinesInProject SUMIP ON M.MachineID = SUMIP.MachineID
        LEFT JOIN projects P ON SUMIP.ProjectID = P.ProjectID
        GROUP BY M.MachineID, M.Hostname, M.IPAddress
        ORDER BY M.MachineID DESC;
    """

        cursor.execute(query, (courseId,))
        result = cursor.fetchall()
        for row in result:
            print(','.join([str(item) if item else '0' for item in row]))
    except mysql.connector.Error as error:
        pass

    finally:
        cursor.close()
