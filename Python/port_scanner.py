#!/usr/bin/env python3
"""
Simple port scanner - learning for cybersecurity
Beginner-friendly script for learning core concepts through a functional, practical program.
"""

# Import external libary to access its functions and attributes
import socket

open_ports = []
service_info = []
"""
Initialize empty lists for storing info. They will populate when the script executes.
"""

# TODO: add functions
# 1. socket - make a network connection, takes target and port as arguments
# 2. get service info on a port
# 3. print results

def main(): # Defines a function, gives it a name
    """
    Main function - this is where the program starts. NOTE INDENTATION!
    """
    print("Simple Port Scanner") # Print whatever is within quotes to terminal
    
    # Set variable 'target' to whatever user inputs - \n for new line
    target = input("\nEnter a target: ")
    # To-do: make sure a valid IPv4 address is entered
    
    # Set variables for start and end ports based on user input - convert to numbers
    start_port = int(input("Enter a starting port: "))
    end_port = int(input("Enter an ending port: "))
    
    # Printf allows embedding variable values in text printed to terminal
    print(f"\nScanning target {target} ports {start_port} - {end_port}, please wait...")
    
    # TODO: main scanning logic
    
    # TODO: print results

if __name__ == "__main__":
    """
    Special value that allows this script to be run standalone or imported as a module by another
    script. NOTE INDENTATION!
    """
    main()