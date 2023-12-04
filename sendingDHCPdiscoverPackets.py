import socket
import struct
import random
import time

def craft_dhcp_discover():
    dest_mac = b'\xff\xff\xff\xff\xff\xff'
    src_mac = bytes([random.randint(0, 255) for _ in range(6)])
    ethernet_header = struct.pack('!6s6sH', dest_mac, src_mac, 0x0800)

    ip_header = struct.pack('!BBHHHBBH4s4s', 0x45, 0, 0, 0, 0, 64, socket.IPPROTO_UDP, 0, b'\x00\x00\x00\x00', b'\xff\xff\xff\xff')

    udp_header = struct.pack('!HHHH', 68, 67, 0, 0)

    bootp_header = struct.pack('!BBHH4sHH4s', 1, 1, 0, 0, b'\x00\x00\x00\x00', 0, 0, b'\x00\x00\x00\x00')

    dhcp_header = b'\x35\x01\x01'  # DHCP Message Type: Discover

    dhcp_discover_packet = ethernet_header + ip_header + udp_header + bootp_header + dhcp_header

    return dhcp_discover_packet

def send_dhcp_discover(interface, num_packets=1, delay=0.0):
    with socket.socket(socket.AF_PACKET, socket.SOCK_RAW) as s:
        try:
            s.bind((interface, 0))
            for i in range(num_packets):
                dhcp_discover_packet = craft_dhcp_discover()
                s.send(dhcp_discover_packet)
                
                print(f"Packet {i+1} sent:")
                print(f"Destination MAC: {':'.join(format(x, '02x') for x in dhcp_discover_packet[:6])}")
                print(f"Source MAC: {':'.join(format(x, '02x') for x in dhcp_discover_packet[6:12])}")
                print("DHCP Message Type: Discover")
                print("")

                time.sleep(delay)
        except OSError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    interface = input("Enter the network interface (e.g., eth0): ")
    num_packets = int(input("Enter the number of DHCP discover packets to send: "))
    delay = float(input("Enter the delay between packets in seconds: "))

    send_dhcp_discover(interface, num_packets, delay)

