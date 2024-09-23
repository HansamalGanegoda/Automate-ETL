import os
import mysql.connector
from datetime import datetime

# MySQL connection details
db_config = {
    'host': 'mysql-etl',  # MySQL container name
    'user': 'root',
    'password': 'root',
    'database': 'etl_db'
}

# Folder to monitor (this is the mounted path in the container)
source_folder = '/app/source_data'  # Path inside the Docker container

try:
    # Connect to MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Extract and Process Files
    for file_name in os.listdir(source_folder):
        if file_name.endswith('.csv'):
            transfer_date = datetime.now()
            print(f'Processing file: {file_name}...')

            # Insert file record into source_files table
            cursor.execute("INSERT INTO source_files (file_name, transfer_date, status) VALUES (%s, %s, %s)",
                           (file_name, transfer_date, 'transferred'))
            conn.commit()

            # Transform and Load
            try:
                with open(os.path.join(source_folder, file_name), 'r') as file:
                    data = file.read()  # Dummy transformation; replace with actual processing logic

                    # Insert processed data into transformed_data table
                    cursor.execute("INSERT INTO transformed_data (file_id, processed_data) VALUES (%s, %s)",
                                   (cursor.lastrowid, data))
                    conn.commit()
                    print(f'Successfully processed and loaded: {file_name}')
            except Exception as e:
                print(f'Error processing file {file_name}: {e}')

    print('ETL process completed successfully.')

except mysql.connector.Error as err:
    print(f'Error connecting to MySQL: {err}')
finally:
    # Clean up
    cursor.close()
    conn.close()
