# Automate ETL Process

## Overview
This project automates the ETL (Extract, Transform, Load) process using MySQL and Docker. It monitors a specified folder for CSV files, processes them, and loads the data into a MySQL database.

## Prerequisites
- [Docker](https://www.docker.com/get-started)
- Basic knowledge of SQL and Python

## Project Structure

## Setup Instructions

### Step 1: Create a Docker Network
Create a Docker network to allow communication between containers:
```bash
docker network create etl_network
Step 2: Build the Docker Image
Navigate to the project directory and run:


docker build -t etl-script .
Step 3: Run the MySQL Container

docker run --name mysql-etl -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=etl_db --network etl_network -d mysql:latest
Step 4: Create Database Tables
Access the MySQL shell and create the required tables:


docker exec -it mysql-etl mysql -uroot -proot -e "USE etl_db; CREATE TABLE source_files (id INT AUTO_INCREMENT PRIMARY KEY, file_name VARCHAR(255), transfer_date DATETIME, status VARCHAR(50)); CREATE TABLE transformed_data (id INT AUTO_INCREMENT PRIMARY KEY, file_id INT, processed_data TEXT, FOREIGN KEY (file_id) REFERENCES source_files(id));"
Step 5: Run the ETL Process
Run the ETL container that processes the CSV files:


docker run --network etl_network --name etl-container -v "C:\Users\sasindu\Desktop\Automate ETL process:/app/source_data" etl-script
Step 6: View Logs
Check the logs to see the output of the ETL process:


docker logs etl-container
Step 7: Clean Up (if needed)
If you need to stop and remove containers, you can use:


docker stop etl-container
docker rm etl-container
docker stop mysql-etl
docker rm mysql-etl
