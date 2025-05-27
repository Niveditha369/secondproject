Project: Basic Network Scanner (Sniff_Tool.py)

Overview:
The Sniff_Tool.py script is a command-line utility designed to scan a specified local network segment. It identifies active devices by sending ARP requests and listening for responses, providing a list of connected devices with their local IP addresses and corresponding MAC addresses. The enhanced version also attempts to resolve hostnames for better identification.

Capabilities:

Device Discovery: Scans a given IP address range (subnet) to find active devices.
IP Address Identification: Lists the local IP address of each responding device.
MAC Address Identification: Provides the unique MAC address for each discovered device.
Hostname Resolution (Enhanced): Attempts to resolve the hostname for each IP address, offering more descriptive information.
Command-Line Interface: Easy to use via command-line arguments for specifying the target network.

Prerequisites:
To run this tool, you need to have Python installed on your system. Additionally, the following Python libraries and network drivers are required:

argparse: A standard Python library for parsing command-line arguments. (Usually comes with Python, no separate install needed).
scapy: A powerful interactive packet manipulation program.
Installation: pip install scapy
Npcap (for Windows users): This is a crucial network packet capture library that scapy relies on for low-level network access on Windows.
Installation: Download and install Npcap from https://nmap.org/npcap/. During installation, ensure you select the option "Install Npcap in WinPcap API-compatible Mode" (or similar). A system restart after installation is often recommended.
Important Note on Privileges:
This tool requires root (on Linux/macOS) or administrative (on Windows) privileges to perform network sniffing and sending operations at Layer 2. You must run the command prompt or terminal with these elevated permissions.

How to Use:
Save the Code: Save the code above into a file named Sniff_Tool.py (or any .py extension).
Open Terminal/Command Prompt with Administrator Privileges:

Windows: Search for "Command Prompt" or "PowerShell", right-click, and select "Run as administrator."
Linux/macOS: Open your terminal. You will typically use sudo before the python command.
Navigate to the Script's Directory: Use the cd command to change your current directory to where you saved Sniff_Tool.py.

Example (Windows): cd C:\Users\YourUsername\Documents
Example (Linux/macOS): cd /home/yourusername/scripts
Execute the Script:
Use the following syntax, replacing <file_name> with Sniff_Tool.py and <ip_address>/<subnet> with your network's details.

Syntax:
python <file_name> -ip <ip_address>/<subnet>

Example (Windows):
python Sniff_Tool.py -ip 192.168.1.1/24

Example (Linux/macOS):
sudo python Sniff_Tool.py -ip 192.168.1.1/24
(Note: Replace 192.168.1.1/24 with the actual IP address of your router/default gateway and its subnet mask. You can find your "Default Gateway" by running ipconfig on Windows or ip r or route -n on Linux/macOS.)

Example Output:
Here's a sample output you might see when running the enhanced Sniff_Tool.py on a typical home network:
Scanning network for active devices on 192.168.1.1/24...

Active devices found:

IP Address           MAC Address        Hostname

192.168.1.1          7c:a9:6b:07:6e:14  MyHomeRouter
192.168.1.3          88:11:96:ff:79:a0  LivingRoomSpeaker
192.168.1.10         68:db:f5:84:80:7f  My-Smartphone
192.168.1.14         a4:c3:f0:4f:a5:06  DESKTOP-XYZ456
192.168.1.26         28:6c:07:8c:96:f5  SmartTV-Samsung
192.168.1.2          6c:56:97:b0:fe:b3  MyLaptop
