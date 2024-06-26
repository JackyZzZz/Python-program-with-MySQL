import mysql.connector
import sys
from constants import Constants
import initialization
import import_data
import insert_use
import updateCourse
import listCourse
import popularCourse
import adminEmails
import activeStudent
import insert_student
import machineUsage
import add_email
import delete_student
import insert_machine

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 project.py <function name> [params]")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name == 'import':
        # python project.py import test_data
        folder_name = sys.argv[2]
        initialization.initialize_database()
        conn = initialization.connect()
        import_data.import_data(folder_name, conn)
        conn.close()

    if function_name == 'insertUse':
        # Success: python project.py insertUse 2 aanthony4 1 2024-03-01 2024-03-15
        # Fail: python project.py insertUse NULL NULL NULL 2024-03-01 2024-03-15
        # Fail: python project.py insertUse 999 aanthony4 1 2024-03-01 2024-03-15
        projectId = int(sys.argv[2]) if sys.argv[2] != 'NULL' else None
        studentUCINetID = sys.argv[3]
        machineId_1 = int(sys.argv[4]) if sys.argv[4] != 'NULL' else None
        start_date = sys.argv[5]
        end_date = sys.argv[6]
        conn = initialization.connect()
        insert_use.insertUse(projectId, studentUCINetID, machineId_1, start_date, end_date, conn)
        conn.close()

    if function_name == 'updateCourse':
        # Success: python project.py updateCourse 1 NULL
        # Success: python project.py updateCourse 1 "Database Management"
        # Fail: python project.py updateCourse NULL "Database Management"
        # Fail: python project.py updateCourse 2 'This is a test string that is intentionally made very long to exceed the VARCHAR(100) limit. Let us see what happens when it is inserted.'
        courseId_1 = int(sys.argv[2]) if sys.argv[2] != 'NULL' else None
        title = sys.argv[3]
        conn = initialization.connect()
        updateCourse.updateCourse(courseId_1, title, conn)
        conn.close()

    if function_name == 'listCourse':
        # python project.py listCourse mchang13
        studentID = sys.argv[2]
        conn = initialization.connect()
        listCourse.listCourse(studentID, conn)
        conn.close()

    if function_name == 'popularCourse':
        # python project.py popularCourse 3
        topN = int(sys.argv[2])
        conn = initialization.connect()
        popularCourse.popularCourse(topN, conn)
        conn.close()

    if function_name == 'adminEmails':
        machineId_2 = int(sys.argv[2])
        conn = initialization.connect()
        adminEmails.adminEmails(machineId_2, conn)
        conn.close()

    if function_name == 'activeStudent':
        machineId_3 = int(sys.argv[2])
        N = int(sys.argv[3])
        startDate = sys.argv[4]
        endDate = sys.argv[5]
        conn = initialization.connect()
        activeStudent.activeStudent(machineId_3, N, startDate, endDate, conn)
        conn.close()

    if function_name == 'machineUsage':
        courseId_2 = int(sys.argv[2])
        conn = initialization.connect()
        machineUsage.machineUsage(courseId_2, conn)
        conn.close()

    if function_name == 'insertStudent':
        # Success: python project.py insertStudent testID test@uci.edu Alice NULL Wang
        # Success: python project.py insertStudent testID test@uci.edu NULL NULL NULL
        # Fail: python project.py insertStudent NULL test@uci.edu Alice NULL Wang
        # Fail: python project.py insertStudent testID NULL Alice NULL Wang
        if len(sys.argv) != 7:
            print(
                "Usage: python3 project.py insertStudent [UCINetID] [email] [First] [Middle] [Last]")
            sys.exit(1)

        UCINetID = sys.argv[2]
        email = sys.argv[3]
        first_name = sys.argv[4]
        middle_name = sys.argv[5] if sys.argv[5] != 'NULL' else None
        last_name = sys.argv[6]
        conn = initialization.connect()
        result = insert_student.insertStudent(UCINetID, email, first_name, middle_name, last_name,
                                              conn)
        print('Success' if result else 'Fail')
        conn.close()

    if function_name == 'addEmail':
        # Fail: python project.py addEmail testID NULL
        # Fail: python project.py addEmail NULL test@gmail.com
        # Success: python project.py addEmail testID test@gmail.com
        # Fail: python project.py addEmail testID test@gmail.com

        UCINetID = sys.argv[2]
        email = sys.argv[3]
        conn = initialization.connect()
        result = add_email.addEmail(UCINetID, email, conn)
        conn.close()

    if function_name == 'deleteStudent':
        # python project.py deleteStudent testID
        UCINetID = sys.argv[2]
        conn = initialization.connect()
        result = delete_student.deleteStudent(UCINetID, conn)
        conn.close()

    if function_name == 'insertMachine':
        # python project.py insertMachine 102 test.com 192.168.10.5 Active "DBH 1011"
        # python project.py insertMachine 1024 NULL NULL NULL NULL
        MachineID = int(sys.argv[2]) if sys.argv[2] != 'NULL' else None
        hostname = sys.argv[3]
        IPAddr = sys.argv[4]
        status = sys.argv[5]
        location = sys.argv[6]
        conn = initialization.connect()
        result = insert_machine.insertMachine(MachineID, hostname, IPAddr, status, location, conn)
        conn.close()

if __name__ == "__main__":
    main()