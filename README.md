# CodeAlpha Basic Network Sniffer

## CodeAlpha Cyber Security Internship — Task 1

### Project Description

This project is a basic network sniffer developed in Python using the Scapy library.

The program captures network packets on the `eth0` interface and displays useful information about the captured traffic.

### Objectives

The objectives of this project are:

* Capture network traffic packets.
* Analyze captured packets.
* Display source and destination IP addresses.
* Identify common network protocols.
* Display available packet payload information.
* Understand how data flows through a network.

### Technologies Used

* Python 3
* Scapy
* Kali Linux

### Network Interface

The sniffer was configured to capture traffic through:

```text
eth0
```

### Information Displayed

For captured IP packets, the program displays:

* Source IP address
* Destination IP address
* Protocol
* Payload information

The program can identify:

* TCP
* UDP
* ICMP
* Other IP traffic

### How to Run

First, open the project directory:

```bash
cd ~/CodeAlpha_BasicNetworkSniffer
```

Run the sniffer with administrator privileges:

```bash
sudo python3 sniffer.py
```

The program starts capturing packets and displays the captured information in the terminal.

To stop packet capture:

```text
CTRL + C
```

### Project Files

```text
CodeAlpha_BasicNetworkSniffer/
│
├── sniffer.py
├── README.md
└── screenshots/
    └── packet_capture.png
```

### Evidence

A screenshot of the packet-capturing output is included in the `screenshots` folder.

### Conclusion

This project provided practical experience with network packet capture and basic packet analysis using Python and Scapy. It demonstrates how information such as IP addresses, protocols, and payload data can be observed from network traffic in a controlled environment.

### Internship

**CodeAlpha — Cyber Security Internship**

**Task:** Basic Network Sniffer

