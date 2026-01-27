import socket

domain = input("Մուտքագրիր domain-ը: ").strip()
subdomains = ["www", "admin", "test", "dev", "mail"]

for sub in subdomains:
    full_domain = f"{sub}.{domain}"

    try:
        ip = socket.gethostbyname(full_domain)
        print(f"[+] FOUND: {full_domain} -> {ip}")
    except socket.gaierror:
        pass
