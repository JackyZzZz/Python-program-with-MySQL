import mysql.connector

def insertMachine(MachineID, hostname, IPAddr, status, location, conn):
    cursor = conn.cursor()
    try:
        insert_machine_query = """
        INSERT INTO machines (MachineID, Hostname, IPAddress, OperationalStatus, Location)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Handle NULL values
        MachineID_value = None if MachineID == 'NULL' else MachineID
        hostname_value = None if hostname == 'NULL' else hostname
        IPAddr_value = None if IPAddr == 'NULL' else IPAddr
        status_value = None if status == 'NULL' else status
        location_value = None if location == 'NULL' else location

        cursor.execute(insert_machine_query, (MachineID_value, hostname_value, IPAddr_value, status_value, location_value))
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

