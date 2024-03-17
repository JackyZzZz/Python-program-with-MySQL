# UpdateCourse.py

import mysql.connector

def updateCourse(courseId, title, conn):
    """
    Update the title of a course
    """

    cursor = conn.cursor()
    try:
        query = "UPDATE courses SET Title = %s WHERE CourseId = %s"

        # Handle NULL values
        courseId_values = None if courseId == 'NULL' else courseId
        title_values = None if title == 'NULL' else title

        cursor.execute(query, (title_values, courseId_values))
        conn.commit()

        if cursor.rowcount == 0:
            print('Fail')
        else:
            print('Success')
    except mysql.connector.Error as error:
        conn.rollback()
        print('Fail')

    finally:
        cursor.close()