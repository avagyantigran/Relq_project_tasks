import socket

target_ip = input("Enter Metasploitable IP address: ")
output_file = "scan_results.txt"

socket.setdefaulttimeout(0.5)

print(f"\nScanning target: {target_ip}\n")

with open(output_file, "w") as file:
    file.write(f"Port scan results for {target_ip}\n")
    file.write("-" * 30 + "\n")

    for port in range(1, 555):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} is OPEN")
            file.write(f"Port {port} is OPEN\n")
        else:
            print(f"Port {port} is CLOSED")

        s.close()

print("\nScan completed.")
print(f"Results saved in {output_file}")
