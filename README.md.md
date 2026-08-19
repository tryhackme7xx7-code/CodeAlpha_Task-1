# **CodeAlpha Basic Network Sniffer**



## &#x20;CodeAlpha Cyber Security Internship — Task 1



### &#x20;Project Description



This project is a basic network sniffer developed in Python using the Scapy library.



The program captures network packets on the `eth0` network interface and displays useful information about the captured traffic.



##### &#x20;Objectives



\* Capture network traffic packets.

\* Analyze captured packets.

\* Display source IP addresses.

\* Display destination IP addresses.

\* Identify network protocols.

\* Display available payload information.

\* Understand how data flows through a network.



\### Technologies Used



\* Python 3

\* Scapy

\* Kali Linux



\### Network Interface



The network interface used for packet capture is:



```text

eth0

```



\### Information Displayed



The program displays:



\* Source IP

\* Destination IP

\* Protocol

\* Payload information



The program identifies common protocols including:



\* TCP

\* UDP

\* ICMP

\* Other IP traffic



\### How to Run



Open a terminal and navigate to the project folder:



```bash

cd CodeAlpha\_BasicNetworkSniffer

```



Run the network sniffer with administrator privileges:



```bash

sudo python3 sniffer.py

```



The program will start capturing packets and displaying their information.



To stop the packet capture:



```text

CTRL + C

```



\### Project Structure



```text

CodeAlpha\_BasicNetworkSniffer/

│

├── sniffer.py

├── README.md

└── screenshots/

&#x20;   └── packet\_capture.png

```



\### Evidence



The `screenshots` folder contains a screenshot showing the network sniffer capturing packets and displaying packet information.



\### Conclusion



This project provided practical experience with network packet capture and basic packet analysis using Python and Scapy.



It demonstrates how source IP addresses, destination IP addresses, protocols, and payload information can be observed from network traffic in a controlled environment.



\### Internship Information



\*\*Organization:\*\* CodeAlpha

\*\*Domain:\*\* Cyber Security

\*\*Task:\*\* Basic Network Sniffer



