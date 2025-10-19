#!/usr/bin/python3
"""Script to create the alx_book_store database"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (use your correct password)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="munde@006"  # your MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
