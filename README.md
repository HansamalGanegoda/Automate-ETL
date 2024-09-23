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
