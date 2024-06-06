import socket
import threading
from art import text2art

ascii_art = text2art("Axt0n Port Scanner V1")
print(ascii_art)

target = input("Enter Target IP Adress: ")

port_range = (1, 9999)

def scan_port(port):
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close

def port_scanner():
    for port in range(port_range[0], port_range[1] + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        thread.start()

if __name__ == "__main__":
    port_scanner()