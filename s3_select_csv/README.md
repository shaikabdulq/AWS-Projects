
# S3 CSV Data Retriever

## Overview
This project involves a Python script that interacts with an AWS S3 bucket to process data from a CSV file. The CSV file is stored in the S3 bucket and the script uses the `boto3` library to query and handle the data.

## Files in the Project
1. `main.py` - The main Python script that uses AWS SDK (`boto3`) to access an S3 bucket, perform an SQL query on the CSV file, and output the results.
2. `employees2.csv` - A CSV file containing sample data about employees, including fields like `Name`, `PhoneNumber`, `City`, and `Occupation`.

## How it Works
- The `main.py` script connects to an S3 bucket (`csv-bucket-to-ddb`) and accesses the `employees2.csv` file.
- It then performs an SQL-like query to select all records from the CSV file.
- The query results are returned in JSON format and are printed out.

## Requirements
- AWS account with access to S3.
- `boto3` library for AWS interaction.
- Python environment to run the script.

## Usage
Run `main.py` to fetch and display data from the `employees2.csv` file stored in the specified S3 bucket.

