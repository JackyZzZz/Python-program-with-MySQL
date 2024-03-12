import mysql.connector

def listCourse(UCINetID, conn):
    """
    List all unique courses that a student is enrolled in, ordered by courseId ascending
    """

    cursor = conn.cursor()
    try:
        query = """
        SELECT DISTINCT C.CourseID, C.Title, C.Quarter 
        FROM StudentUseMachinesInProject SUMIP 
        JOIN projects P ON SUMIP.ProjectId = P.ProjectId 
        JOIN courses C ON P.CourseID = C.CourseID 
        WHERE SUMIP.StudentUCINetID = %s 
        ORDER BY C.CourseID ASC
        """

        cursor.execute(query, (UCINetID,))
        result = cursor.fetchall()
        for row in result:
            print(','.join([str(item) for item in row]))
    except mysql.connector.Error as error:
        pass

    finally:
        cursor.close()