import mysql.connector
import sys
from constants import Constants
import initialization
import import_data
import insert_use

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 project.py <function name> [params]")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name == 'import':
        folder_name = sys.argv[2]
        initialization.initialize_database()
        conn = initialization.connect()
        import_data.import_data(folder_name, conn)
        conn.close()

    if function_name == 'insertUse':
        # Success: python project.py insertUse 2 aanthony4 1 2024-03-01 2024-03-15
        # Fail: python project.py insertUse 999 aanthony4 1 2024-03-01 2024-03-15
        projectId = int(sys.argv[2])
        studentUCINetID = sys.argv[3]
        machineId = int(sys.argv[4])
        start_date = sys.argv[5]
        end_date = sys.argv[6]
        conn = initialization.connect()
        insert_use.insertUse(projectId, studentUCINetID, machineId, start_date, end_date, conn)
        conn.close()

if __name__ == "__main__":
    main()