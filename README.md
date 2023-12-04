# DHCP Discover Sender

A Python script for sending DHCP Discover packets over a network using raw sockets.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Disclaimer](#disclaimer)
- [Author](#author)
- [License](#license)

## Introduction

This script allows you to simulate a client's DHCP (Dynamic Host Configuration Protocol) request for network configuration by sending DHCP Discover packets over a specified network interface. It is a simple tool for educational and testing purposes.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ishaiva/DHCPstarvation.git 
   cd DHCP_Starvation

### Run the script:

    ```bash

    python sendingDHCPdiscoverPackets.py

    Follow the prompts:
        Enter the network interface (e.g., eth0).
        Enter the number of DHCP discover packets to send.
        Enter the delay between packets in seconds.

### Prerequisites

    Python 3.x
    Linux (due to the use of raw sockets)

## How It Works

The script constructs DHCP Discover packets with randomized source MAC addresses and sends them over the specified network interface. The user is prompted to input the necessary parameters such as the network interface, number of packets, and delay.
Getting Started

To get started with the script, follow the Usage instructions. Ensure you have the required prerequisites installed.
Disclaimer

This script is intended for educational and testing purposes only. Misuse of this script may violate network policies or applicable laws. Use responsibly and only on networks you have permission to test.

### Author

ishaiva

### License

This project is licensed under the MIT License - see the LICENSE file for details.

GitHub ishaiva and update the author's name accordingly. Feel free to customize the content further to suit your preferences and provide any additional information you find relevant.


