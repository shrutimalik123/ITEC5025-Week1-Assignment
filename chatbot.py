"""
Course: ITEC5025
Assignment: Week 1 - Basic Python Program
Author: Shruti Malik
Date: 2026-01-12

Description: 
This script initializes the fundamental structure for a chatbot application.
It demonstrates basic output functionality, error handling, and modular design
by printing a formatted "Hello, World!" message to the console.
"""

import sys

def initiate_greeting():
    """
    Function to display the startup message.
    It uses a try-except block to demonstrate graceful error handling.
    """
    try:
        # Define the core message variable
        greeting_message = "Hello, World!"
        
        # Print the message with additional formatting (Distinguished criteria)
        print("-" * 30)
        print(f"SYSTEM STATUS: ONLINE")
        print(f"OUTPUT: {greeting_message}")
        print("-" * 30)
        
    except Exception as e:
        # Gracefully handle any unexpected errors during output
        print(f"An error occurred while attempting to greet: {e}")

# This block ensures the code runs only when executed directly
if __name__ == "__main__":
    initiate_greeting()
