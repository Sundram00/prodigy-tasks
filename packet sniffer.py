from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        if proto == 6:  # TCP
            protocol = "TCP"
        elif proto == 17:  # UDP
            protocol = "UDP"
        else:
            protocol = "Other"

        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")

        if protocol == "TCP" or protocol == "UDP":
            payload = packet[protocol].payload
            print(f"Payload: {payload}")

        print("-" * 50)

def main():
    interface = input("Enter the interface to sniff on (e.g., eth0, wlan0): ")
    print(f"Sniffing on {interface}...")
    sniff(iface=interface, prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
