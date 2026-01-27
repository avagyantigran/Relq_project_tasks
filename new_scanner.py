import socket
import sys
from datetime import datetime
 
# ======================
# TARGET INPUT
# ======================
target = input("Մուտքագրիր IP կամ hostname: ")
 
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("❌ Չհաջողվեց գտնել target-ը")
    sys.exit()
 
print("=" * 50)
print(f"Mini Nmap Scan Report for {target_ip}")
print(f"Scan started at: {datetime.now()}")
print("=" * 50)
 
# ======================
# PORT RANGE
# ======================
start_port = int(input("Սկզբի պորտ (օր. 20): "))
end_port   = int(input("Վերջի պորտ (օր. 100): "))
 
# ======================
# SERVICE DICTIONARY
# ======================
services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NETBIOS",
    143: "IMAP",
    443: "HTTPS",
    3306: "MYSQL",
    3389: "RDP"
}
 
# ======================
# PORT SCAN
# ======================
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
 
    result = s.connect_ex((target_ip, port))
 
    if result == 0:
        service = services.get(port, "UNKNOWN")
        print(f"[+] Port {port}/tcp OPEN  ({service})")
 
    s.close()
 
print("\nScan finished.")
