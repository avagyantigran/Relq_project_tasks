import re

def identify_hash(hash_string):
    # Remove any extra spaces the user might have added
    hash_string = hash_string.strip()
    length = len(hash_string)

    print(f"\n[*] Analyzing hash: {hash_string}")
    print(f"[*] Length detected: {length} characters")

    # We use 'if' statements to check the length
    if length == 32:
        print("[+] Result: This is likely an MD5 hash.")
    elif length == 40:
        print("[+] Result: This is likely a SHA-1 hash.")
    elif length == 64:
        print("[+] Result: This is likely a SHA-256 hash.")
    elif length == 128:
        print("[+] Result: This is likely a SHA-512 hash.")
    else:
        print("[-] Result: Unknown hash type or not a standard hash.")

# This lets the user type in the hash when they run the script
user_input = input("Enter the hash you want to identify: ")
identify_hash(user_input)

