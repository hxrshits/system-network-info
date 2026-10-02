# 🖥️ System Network Info

A Python-based Linux CLI tool that collects and displays system and network information for basic diagnostics, monitoring, and troubleshooting.

This project is built and tested in Linux/Ubuntu through WSL2 and focuses on practical Linux and networking fundamentals.

---

## 🚀 Features

- 🖥️ System information
- 🌐 Primary IPv4 address
- 🔌 Network interfaces
- 🚪 Default gateway
- 🛣️ Routing table
- 🔎 DNS resolution test
- 🔐 Listening TCP/UDP ports
- 🔗 Active network connections
- ⚙️ CPU usage
- 🧠 Memory usage
- 💾 Disk usage
- ⏱️ System uptime
- 📋 Interactive CLI menu
- 🛡️ Basic command error handling

---

## 🛠️ Technologies Used

- Python 3
- Linux
- Linux networking commands
- psutil
- WSL2
- Git & GitHub

---

## 📂 Project Structure

system-network-info/
├── network_info.py
├── requirements.txt
├── .gitignore
└── README.md

---

## 💻 Requirements

- Linux / Ubuntu
- Python 3
- pip
- ip command
- ss command

The project can also be run using Ubuntu through WSL2 on Windows.

---

## ⚙️ Installation

### 1. Clone the repository

    git clone https://github.com/hxrshits/system-network-info.git
    cd system-network-info

### 2. Create a virtual environment

    python3 -m venv .venv

### 3. Activate the virtual environment

    source .venv/bin/activate

### 4. Install dependencies

    pip install -r requirements.txt

---

## ▶️ Usage

Run the application:

    python network_info.py

The program provides an interactive menu:

    ========================================
           SYSTEM NETWORK INFO
    ========================================
    1. System Information
    2. Network Information
    3. Default Gateway
    4. Routing Table
    5. DNS Test
    6. Listening Ports
    7. Active Connections
    8. System Health
    9. Full Report
    0. Exit
    ========================================

Select an option by entering its number.

---

## 📊 Information Collected

### System Information

- Hostname
- Operating system
- OS version
- CPU architecture

### Network Information

- Primary IPv4 address
- Network interface
- Available network interfaces
- Interface IP addresses

### Routing Information

- Default gateway
- Routing table
- Network routes
- Network interfaces used for routing

### DNS

Performs a DNS resolution test using google.com and displays the resolved IP address.

### Ports

Displays listening TCP and UDP ports using Linux ss.

### Active Connections

Displays active TCP and UDP network connections.

### System Health

Displays:

- CPU usage
- Memory usage
- Disk usage
- System uptime

---

## 🧠 What I Learned

### Linux

- Linux terminal
- Linux networking commands
- Network interfaces
- IP configuration
- Routing
- Ports and sockets
- System monitoring

### Networking

- IPv4 addressing
- Network interfaces
- Default gateways
- Routing tables
- DNS
- TCP/UDP
- Listening ports
- Active connections

### Python

- Functions
- Modules
- subprocess
- socket
- psutil
- Exception handling
- CLI input
- Structured Python programs

### Development

- Virtual environments
- Dependency management
- Git
- GitHub
- Project documentation

---

## ☁️ Cloud Networking Relevance

This project runs locally on Linux/WSL2 and is not an AWS deployment.

However, the networking concepts practiced in this project are foundational for cloud networking.

| Linux / Networking Concept | Cloud Networking Concept |
|---|---|
| IP Address | Cloud IP addressing |
| Network Interface | Virtual Network Interface |
| Routing Table | Cloud Route Table |
| Default Gateway | Internet/NAT Gateway concepts |
| DNS | Cloud DNS services |
| Listening Ports | Security Group / Firewall rules |
| Network Isolation | VPC / Virtual Network concepts |

The purpose of this project is to build a strong Linux and networking foundation before moving deeper into AWS and cloud networking.

---

## 🔮 Future Improvements

- [ ] Network connectivity testing
- [ ] Ping and latency measurement
- [ ] Packet-loss detection
- [ ] Network traffic statistics
- [ ] Configurable DNS testing
- [ ] JSON output
- [ ] Logging support
- [ ] Exportable reports
- [ ] Additional network diagnostics
- [ ] Optional AWS networking integration

---

## ⚠️ Note

This project is designed as a local Linux networking and system diagnostics tool.

It does not require an AWS account and does not create or deploy AWS resources.

AWS/cloud concepts mentioned in this README are used to explain how the networking fundamentals relate to cloud infrastructure.

---

## 👨‍💻 Author

Harshit Saini

ECE & AIML Undergraduate  

GitHub: https://github.com/hxrshits

---

⭐ If you find this project useful, feel free to explore the repository and follow the development.
