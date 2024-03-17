# popularCourse.py

import mysql.connector

def popularCourse(topN, conn):
    """
    List the top N most popular courses that has most students attended,
    ordered by studentCount, courseID descending
    """

    cursor = conn.cursor()
    try:
        query = """
        SELECT C.CourseID, C.Title, COUNT(SUMIP.StudentUCINetID) AS studentCount
        FROM StudentUseMachinesInProject SUMIP
        JOIN projects P ON SUMIP.ProjectId = P.ProjectId 
        JOIN courses C ON P.CourseID = C.CourseID
        GROUP BY C.CourseID
        ORDER BY COUNT(SUMIP.StudentUCINetID) DESC, C.CourseID DESC
        LIMIT %s
        """

        cursor.execute(query, (topN,))
        result = cursor.fetchall()
        for row in result:
            print(','.join([str(item) for item in row]))

    except mysql.connector.Error as error:
        pass

    finally:
        cursor.close()