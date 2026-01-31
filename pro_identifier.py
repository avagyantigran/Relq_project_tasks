import re

def identify_hash(user_input):
    h = user_input.strip().lower() # Clean the input
    length = len(h)
    
    # Regex patterns: 
    # ^ means start, $ means end, [0-9a-f] means only those characters allowed
    is_hex = re.match(r"^[0-123456789abcdef]+$", h)

    if not is_hex:
        print("[-] Error: This contains non-hexadecimal characters. Not a standard hash.")
        return

    print(f"[*] Analyzing: {h}")
    
    # Logic based on length and hex-check
    if length == 32:
        print("[+] Possible Type: MD5")
    elif length == 40:
        print("[+] Possible Type: SHA-1")
    elif length == 64:
        print("[+] Possible Type: SHA-256")
    elif length == 128:
        print("[+] Possible Type: SHA-512")
    else:
        print("[-] Unknown hash length.")

# Get input from user
target = input("Paste your hash here: ")
identify_hash(target)
