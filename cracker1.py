import hashlib

def crack_hash(target_hash):
    # This is our 'Dictionary' (Common guesses)
    wordlist = ["password", "123456", "admin", "hello", "welcome"]

    print(f"[*] Attempting to crack: {target_hash}")

    for word in wordlist:
        # 1. Take the guess and turn it into an MD5 hash
        # .encode() turns text into bytes for Python
        guess_hash = hashlib.md5(word.encode()).hexdigest()

        # 2. Compare our guess to the target
        if guess_hash == target_hash:
            print(f"[+] Match found! The word is: {word}")
            return
        else:
            print(f"[-] Tried {word}... no match.")

    print("[-] Cracking failed. Word not in our list.")

# Use the MD5 hash for 'hello'
crack_hash("5d41402abc4b2a76b9719d911017c592")
