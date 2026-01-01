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
# 1. socket - make a network connection, takes target and port as arguments - DONE
# 2. get service info on a port
# 3. print results - DONE

def check_port(target, port):
    """
    Try to connect to a port on the target.
    """
    try:
        # Create a socket
        # AF_INET for IPv4 address
        # SOCK_STREAM for TCP packets
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # 1 second timeout

        result = sock.connect_ex((target, port)) # Checks connection state, returns 0 if open

        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port) # Add port to end of list

            sock.close() # Close the socket when done
            return True
        
        sock.close() # If the port is closed, close the socket anyway
        return False

    # If trying the socket connection doesn't work for some reason, return False and continue
    except:
        return False

def print_results(target):
    """
    Print results of what we find from a target
    """
    print(f"Scan results for: {target}")
    print(f"\nOpen ports found: {len(open_ports)}") # Count the total number of open ports found

    if open_ports: # If the list has data, print details
        print("\nPort details:")
        # TODO: get and print info from the port details function
    
    else:
        print("\nNo open ports found.") # Notify user if no open ports were found

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
    
    # TODO: main scanning logic - IN PROGRESS
    for port in range(start_port, end_port +1): # Loop through each port incrementally
        check_port(target, port)
    
    # TODO: print results - DONE
    print_results(target)

if __name__ == "__main__":
    """
    Special value that allows this script to be run standalone or imported as a module by another
    script. NOTE INDENTATION!
    """
    main()