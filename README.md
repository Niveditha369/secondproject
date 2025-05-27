They can check the number of devices connected to your network and print their local IP addresses along with their MAC addresses and hostnames.

Sniff_Tool.py
I have used argparse and scapy to make this basic network scanner.

Syntax :
    python <file_name> -ip <ip_address>/<subnet>

NOTE : Use it with root/administrative priviledges

One needs to have argparse and scapy installed.

They can be installed with :

pip install argparse

pip install scapy

OUTPUT :

{'ip': '192.168.1.1', ' mac': '7c:a9:6b:07:6e:14'}

{'ip': '192.168.1.3', ' mac': '88:11:96:ff:79:a0'}

{'ip': '192.168.1.10', ' mac': '68:db:f5:84:80:7f'}

{'ip': '192.168.1.4', ' mac': 'd4:f5:47:17:b0:a6'}

{'ip': '192.168.1.14', ' mac': 'a4:c3:f0:4f:a5:06'}

{'ip': '192.168.1.2', ' mac': '6c:56:97:b0:fe:b3'}

{'ip': '192.168.1.26', ' mac': '28:6c:07:8c:96:f5'}
