import mysql.connector

def updateCourse(courseId, title, conn):
    """
    Update the title of a course
    """

    cursor = conn.cursor()
    try:
        query = "UPDATE courses SET Title = %s WHERE CourseId = %s"
        cursor.execute(query, (title, courseId))
        conn.commit()
        print('Success')
    except mysql.connector.Error as error:
        print('Fail')

    finally:
        cursor.close()