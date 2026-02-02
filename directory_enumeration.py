import requests

target_url = "http://10.0.2.3"
wordlist = ["admin", "login", "config", "backup", "php", "uploads", "phpMyAdmin"]

for word in wordlist:
    url = f"{target_url}/{word}"
    try:
        response = requests.get(url, timeout=3)

        if response.status_code in [200, 301, 302, 403]:
            print(f"[+] Found Directory: {url} ({response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"[-] Error accessing {url}: {e}")
