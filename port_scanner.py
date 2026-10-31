
import socket
from datetime import datetime

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((target, port))
        return result == 0
    except socket.error:
        return False
    finally:
        sock.close()


target = input("Enter your own computer IP (use 127.0.0.1 for practice): ").strip()

try:
    socket.inet_aton(target)

    print("\n===== PYTHON NETWORK PORT SCANNER =====")
    print("Target:", target)
    print("Scan started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    open_ports = []

    # Scan a small range of ports on your own computer
    for port in range(1, 101):
        if scan_port(target, port):
            open_ports.append(port)
            print(f"Port {port}: OPEN")

    print("\n===== SCAN SUMMARY =====")
    print("Ports checked: 100")
    print("Open ports found:", len(open_ports))

    with open("scan_report.txt", "w") as report:
        report.write("PYTHON NETWORK PORT SCANNER REPORT\n")
        report.write(f"Target: {target}\n")
        report.write("Ports checked: 1-100\n")
        report.write(f"Open ports: {open_ports}\n")

    print("Report saved as scan_report.txt")

except OSError:
    print("Invalid IPv4 address. Please try again.")
