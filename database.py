"""
This module provides functions for connecting to and interacting with a SQLite
database.

Functions:
connect(): Connects to a SQLite database and returns a connection object.
check_data(connection, input_data): Checks if the input data already exists in
the database.
update_data(connection, input_data): Updates the relevant entry in the database
with new input data.
insert_data(connection, input_data): Inserts new data into the database.
"""
import sqlite3

def connect():
    """
    Connect to the SQLite database.

    Returns:
    sqlite3.Connection: connection object to interact with the SQLite database.
    """
    # Connect to the SQLite database
    connection = sqlite3.connect("database.db")
    return connection

def check_data(connection, input_data):
    """
    Check if the input data already exists in the database.

    Args:
    connection (sqlite3.Connection): connection object to interact with the
    SQLite database.
    input_data (str): input data to be searched in the database.

    Returns:
    bool: True if input data already exists in the database, False otherwise.
    """
    # Create cursor
    cursor = connection.cursor()

    # Check if data already exists in the database
    cursor.execute("SELECT * FROM data WHERE input_data=?", (input_data,))
    data = cursor.fetchone()

    if data:
        return True
    else:
        return False

def update_data(connection, input_data):
    """
    Update the relevant entry in the SQLite database with new input data.

    Args:
    connection (sqlite3.Connection): connection object to interact with the
    SQLite database.
    input_data (str): new input data to be updated.
    """
    # Create cursor
    cursor = connection.cursor()

    # Update the relevant entry in the database
    cursor.execute("UPDATE data SET input_data=? WHERE input_data=?",
     (input_data, input_data))
    connection.commit()

def insert_data(connection, input_data) -> None:
    """
    Inserts new data into the SQLite database.

    Args:
    connection (sqlite3.Connection): The connection to the SQLite database.
    input_data (str): The input data to be inserted into the database.

    Returns:
    None
    """
    # Create cursor
    cursor = connection.cursor()

    # Insert new data into the database
    cursor.execute("INSERT INTO data (input_data) VALUES (?)", (input_data,))
    connection.commit()
