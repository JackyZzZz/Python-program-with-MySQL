import csv

def import_data(folderName, conn):
    """
    Import data from the csv files to the database
    """

    cursor = conn.cursor()
    tables = ['users', 'courses', 'machines', 'students', 'admins', 'emails', 'projects', 'use', 'manage']

    for table in tables:
        if not table == 'use':
            with open(f'{folderName}/{table}.csv', 'r') as file:
                csv_data = csv.reader(file)
                for row in csv_data:
                    row = [None if field == 'NULL' else field for field in row]
                    query = f"INSERT INTO {table} VALUES ({', '.join(['%s'] * len(row))})"
                    # Execute the query with the row data
                    cursor.execute(query, row)
                conn.commit()
        # Special case for the use table
        else:
            with open(f'{folderName}/{table}.csv', 'r') as file:
                csv_data = csv.reader(file)
                for row in csv_data:
                    row = [None if field == 'NULL' else field for field in row]
                    query = f"INSERT INTO StudentUseMachinesInProject VALUES ({', '.join(['%s'] * len(row))})"
                    # Execute the query with the row data
                    cursor.execute(query, row)
                conn.commit()

    counts = dict()
    for table in ['users', 'machines', 'courses']:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]  # fetchone() returns a tuple, get the first item
        counts[table] = count

    print(counts['users'])
    print(counts['machines'])
    print(counts['courses'])
    cursor.close()