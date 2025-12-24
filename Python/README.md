# Practical Python For Cybersecurity

Python is generally considered a good place to start learning programming. I used AI to generate some ideas for a functional script and landed on a port scanner.

## Goals

A port scanner needs to do two things: scan a target and return info about what it scanned. For the purposes of my learning, I'm focusing on
* A single IPv4 target
* A range of ports
* Displaying returned info in the terminal

I may extend the capabilities to include scanning networks using CIDR notation or domains, and also maybe other data consumption features like saving to a file, later.

## Methods

What does my script need to accomplish these goals?
* Take user input - target, ports
* Make a network connection
  * Like a phone call
    - Pick up the phone, initialize a connection
    - Other end hears the request (ringing), they answer
    - Exchange info
    - Hang up and close the connection
  * Python has a library for this (socket)!
* Print results to screen with print and printf