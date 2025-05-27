import sys
import argparse
from scapy.all import scapy, Ether, ARP, srp
import socket # Import the socket module for hostname resolution

parser = argparse.ArgumentParser(description="Network Sniffing Tool")
parser.add_argument("-ip", "--ipadd", help="IP Address/Subnet Mask (e.g., 192.168.1.1/24)")
args = parser.parse_args()

if not args.ipadd:
    print("Invalid Syntax: IP Address/Subnet Mask is required.")
    print("Use --help or -h for options.")
    print("Example: python Sniff_Tool.py -ip 192.168.1.1/24")
    sys.exit(1)
else:
    print(f"Scanning network for active devices on {args.ipadd}...")
    try:
        arp_request = ARP(pdst=args.ipadd)
        broadcast_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
        final_request = broadcast_frame / arp_request

        results_ans, _ = srp(final_request, timeout=2, verbose=False)

        results = []
        for sent_packet, received_packet in results_ans:
            ip = received_packet.psrc
            mac = received_packet.hwsrc
            hostname = "N/A" # Default if resolution fails
            try:
                # Attempt to resolve hostname
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                # Hostname not found for this IP
                pass
            except Exception as e:
                # Other potential errors during resolution
                # print(f"Warning: Could not resolve hostname for {ip}: {e}")
                pass

            clients = {"ip": ip, "mac": mac, "hostname": hostname}
            results.append(clients)

        if results:
            print("\nActive devices found:")
            print("-------------------------------------------------------")
            print(f"{'IP Address':<18} {'MAC Address':<18} {'Hostname':<20}")
            print("-------------------------------------------------------")
            for client in results:
                print(f"{client['ip']:<18} {client['mac']:<18} {client['hostname']:<20}")
            print("-------------------------------------------------------")
        else:
            print("\nNo active devices found on the specified network segment.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please ensure Npcap is installed with 'WinPcap API-compatible Mode' enabled,")
        print("and that you are running the Command Prompt as an administrator.")
