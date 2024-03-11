import mysql.connector
import sys
from constants import Constants
import initialization
import import_data

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

if __name__ == "__main__":
    main()