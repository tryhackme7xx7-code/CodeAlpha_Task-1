from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def packet_callback(packet):
    print("\n" + "=" * 60)

    if IP in packet:
        source = packet[IP].src
        destination = packet[IP].dst

        print(f"Source IP      : {source}")
        print(f"Destination IP : {destination}")

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "Other"

        print(f"Protocol       : {protocol}")

        if Raw in packet:
            payload = bytes(packet[Raw].load)
            print(f"Payload        : {payload[:100]!r}")
        else:
            print("Payload        : No application payload")

    else:
        print("Non-IP packet detected")


print("CodeAlpha - Basic Network Sniffer")
print("Capturing packets on eth0...")
print("Press CTRL+C to stop.\n")

sniff(iface="eth0", prn=packet_callback, store=False)
