# insert_machine.py

import mysql.connector

def insertMachine(MachineID, hostname, IPAddr, status, location, conn):
    cursor = conn.cursor(buffered=True)
    try:
        # Check if MachineID already exists
        check_query = "SELECT * FROM machines WHERE MachineID = %s"
        cursor.execute(check_query, (MachineID,))
        if cursor.rowcount >= 1:
            print('Fail')
            return False

        # If MachineID does not exist, proceed to insert
        insert_machine_query = """
        INSERT INTO machines (MachineID, Hostname, IPAddress, OperationalStatus, Location)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_machine_query, (MachineID, hostname, IPAddr, status, location))
        conn.commit()
        print('Success')
        return True
    except mysql.connector.Error as error:
        conn.rollback()
        print('Fail')
        return False
    finally:
        if cursor is not None:
            cursor.close()

