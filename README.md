# port_scanner
python port scanner.
This is a basic port scanner

Welcome to the Python Port Scanner!

This is a simple command-line tool that allows you to scan a host for open ports. It can be useful for finding open ports on a network, or for testing firewall rules.
Requirements

Python 3.x

Installation

Clone the repository:

    git clone https://github.com/dragonfiretech/port_scanner.git
        
pyfiglet needs to be installed, copy and paste the code below.

    pip install pyfiglet

Navigate to the directory:

The REPO should install in your Home directory so you should be able to cd right into the folder

    cd port_scanner
    
Type the following command into your CLI

    python3 scanner.py

Usage

To scan a host, run the program in CLI and input the target under Host input:
output should look like this below

Host input:x.x.x.x

x.x.x.x : x.x.x.x

please wait, scanning remote host - x.x.x.x
--------------------------------------------------
2023-01-05 20:46:45.289074

port xx: open

port xx: open

port xxx: open

this is always executed

2023-01-05 20:46:47.419644

Scan start time was 2023-01-05 20:46:45.289074

Scan end time was 2023-01-05 20:46:47.419644

Scan total time was 0:00:02.130570

0:00:02.130570

Target has been scanned


Notes

This scanner is a basic scanner so it will only do 1 host at a time until it is updated it will throw an error and crash if multiple hosts are input.

Some hosts may block port scanners or rate limit requests, in which case the tool may not be able to complete a scan.
Port scanning can be considered a malicious activity and is often prohibited by network administrators. Use this tool responsibly and with permission.
