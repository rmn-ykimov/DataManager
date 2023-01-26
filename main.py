import input_validation as iv
import database as db
import sys

def main():
    # Get input from another program's output
    program_output = sys.stdin.read()

    # Validate program's output
    if iv.validate_input(program_output):
        # Connect to the SQLite database
        connect = db.connect()

        # Check if data already exists in the database
        data_exists = db.check_data(connect, program_output)

        if data_exists:
            # Update the relevant entry in the database
            db.update_data(connect, program_output)
            print("Data updated in the database.")
        else:
            # Insert new data into the database
            db.insert_data(connect, program_output)
            print("Data inserted into the database.")
    else:
        print("Invalid program_output, please try again.")

if __name__ == "__main__":
    main()
