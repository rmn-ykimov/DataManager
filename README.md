# DataManager

This project is a script that handles user input and performs various actions
related to a SQLite database.

The script utilizes the database.py module to handle the connection to the
database and perform functions such as checking if data already exists and
updating the database accordingly. Additionally, the script uses the
input_validation.py module to handle input validation by utilizing the
validate_input() function to check if the input data is in the correct format.

# Modules

1. `main.py`:
    This script handles user input and call other functions as needed. It
    contains the main function that runs the program.
2. `input_validation.py`:
    This module handles input validation, it contains functions to validate the
    input data.
        - `validate_input()` function:
            This function checks that input data is entered in the correct
            format. It ensures that the input is inkey-value pair format, where
            the keys are correctly spelled and the values are of the correct
            data type. The function also checks that all required keys are
            present and that the values are within the expected range.
3. `database.py`:
    This module handle the connection to the SQLite database and the functions
    for checking if data already exists and updating the database, as well as
    new functionalities such as deleting or retrieving data from the database.
        - `connect()` function:
            This function will handle the connection to the SQLite database.
        - `check_data()` function:
            This function will check if the input data already exists in the
            database and return a Boolean value indicating whether or not it
            exists.
        - `update_data()` function:
            This function will update the relevant
            entry in the SQLite database if the input data already exists.



# Dependencies

- SQLite3
