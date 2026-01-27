import requests

# Ask user for target URL
target_url = input("Enter target URL (example: http://10.0.2.3): ").strip()

# Fix missing http://
if not target_url.startswith(("http://", "https://")):
    target_url = "http://" + target_url

wordlist = ["admin", "login", "config", "backup", "php", "uploads", "phpMyAdmin"]

print(f"\n[*] Scanning target: {target_url}\n")

for word in wordlist:
    url = f"{target_url}/{word}"
    try:
        response = requests.get(url, timeout=3, allow_redirects=False)

        if response.status_code in [200, 301, 302, 403]:
            print(f"[+] Found Directory: {url} ({response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"[-] Error accessing {url}: {e}")
