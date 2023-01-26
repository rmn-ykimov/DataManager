"""
This module contains functions for validating input data.

Functions:
    validate_input(input_data:str) -> bool: 
        Check if input data is in valid JSON format, returns True if it is,
        False otherwise.
"""
import json

def validate_input(input_data:str) -> bool:
    """
    Check if input data is in valid JSON format.

    Args:
    input_data (str): The input data in string format to be validated

    Returns:
    bool: True if the input data is in valid JSON format, False otherwise.
    """
    # Try to parse input data as JSON object
    try:
        json.loads(input_data)
    # If input data is not in valid JSON format
    except json.decoder.JSONDecodeError:
        # return false
        return False
    # If input data is in valid JSON format
    return True
