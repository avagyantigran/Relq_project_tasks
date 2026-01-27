#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getopt
import hashlib
import sys
import os
import time

print(" ")
print("Python Hash-Cracker")
print("Version 4.0 Stable (Python3 Fixed)")


def info():
    print(" ")
    print("Information:")
    print("[*] Options:")
    print("[*] (-h) Hash")
    print("[*] (-t) Type [See supported hashes]")
    print("[*] (-w) Wordlist")
    print("[*] (-n) Numbers bruteforce")
    print("[*] (-v) Verbose [{WARNING}Slows cracking down!]\n")
    print("[*] Examples:")
    print("[>] python3 Hash-Cracker.py -h <hash> -t md5 -w DICT.txt")
    print("[>] python3 Hash-Cracker.py -h <hash> -t sha384 -n -v")
    print("[*] Supported Hashes:")
    print("[>] md5, sha1, sha224, sha256, sha384, sha512")
    print("[*] That's all folks!\n")


def checkOS():
    if os.name == "nt":
        return "Windows"
    elif os.name == "posix":
        return "posix"
    return "Unknown"


def get_hash_function(hash_type: str):
    hash_type = hash_type.lower().strip()

    algos = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha224": hashlib.sha224,
        "sha256": hashlib.sha256,
        "sha384": hashlib.sha384,
        "sha512": hashlib.sha512,
    }

    return algos.get(hash_type)


class HashCracking:
    def __init__(self):
        self.lineCount = 0

    def saveToFile(self, hash_value: str, key: str):
        solved = False

        # a+ puts pointer at end, so seek(0) is required for reading
        with open("SavedHashes.txt", "a+", encoding="utf-8") as f:
            f.seek(0)

            for solvedHash in f:
                parts = solvedHash.split(":")
                if len(parts) >= 2:
                    saved_key = parts[0].strip()
                    saved_hash = parts[1].strip().lower()
                    if saved_hash == hash_value.strip().lower():
                        solved = True
                        break

            if not solved:
                print("[*] Hash saved to SavedHashes.txt")
                # store as: password:hash
                f.write(f"{key}:{hash_value}\n")

    def hashCrackWordlist(self, userHash, hashType, wordlist, verbose, bruteForce=False):
        start = time.time()
        self.lineCount = 0

        h = get_hash_function(hashType)
        if not h:
            print(f"[-] Is '{hashType}' a supported hash type?")
            sys.exit(1)

        userHash = userHash.strip().lower()

        # -------------------------
        # Numbers brute force mode
        # -------------------------
        if bruteForce:
            while True:
                candidate = str(self.lineCount)
                candidate_hash = h(candidate.encode("utf-8")).hexdigest().strip().lower()

                if verbose:
                    sys.stdout.write("\r" + candidate + " " * 20)
                    sys.stdout.flush()

                if candidate_hash == userHash:
                    end = time.time()
                    print(f"\n[+] Hash is: {candidate}")
                    print(f"[*] Time: {round(end - start, 2)} seconds")
                    self.saveToFile(candidate_hash, candidate)
                    sys.exit(0)

                self.lineCount += 1

        # -------------------------
        # Wordlist mode
        # -------------------------
        else:
            try:
                with open(wordlist, "r", encoding="utf-8", errors="ignore") as infile:
                    for line in infile:
                        line = line.strip()
                        if not line:
                            continue

                        lineHash = h(line.encode("utf-8")).hexdigest().strip().lower()

                        if verbose:
                            sys.stdout.write("\r" + line + " " * 20)
                            sys.stdout.flush()

                        if lineHash == userHash:
                            end = time.time()
                            print(f"\n[+] Hash is: {line}")
                            print(f"[*] Words tried: {self.lineCount}")
                            print(f"[*] Time: {round(end - start, 2)} seconds")
                            self.saveToFile(lineHash, line)
                            sys.exit(0)

                        self.lineCount += 1

                end = time.time()
                print("\n[-] Cracking Failed")
                print("[*] Reached end of wordlist")
                print(f"[*] Words tried: {self.lineCount}")
                print(f"[*] Time: {round(end - start, 2)} seconds")
                sys.exit(0)

            except FileNotFoundError:
                print("\n[-] Couldn't find wordlist")
                print("[*] Is this right?")
                print(f"[>] {wordlist}")
                sys.exit(1)


def main(argv):
    hashType = None
    userHash = None
    wordlist = None
    verbose = False
    numbersBruteForce = False

    print(f"[Running on {checkOS()}]\n")

    try:
        opts, args = getopt.getopt(argv, "ih:t:w:nv")
    except getopt.GetoptError:
        print("[*] python3 Hash-Cracker.py -t <type> -h <hash> -w <wordlist>")
        print("[*] Type python3 Hash-Cracker.py -i for information")
        sys.exit(1)

    for opt, arg in opts:
        if opt == "-i":
            info()
            sys.exit(0)
        elif opt == "-t":
            hashType = arg.strip().lower()
        elif opt == "-h":
            userHash = arg.strip().lower()
        elif opt == "-w":
            wordlist = arg
        elif opt == "-v":
            verbose = True
        elif opt == "-n":
            numbersBruteForce = True

    if not (hashType and userHash):
        print("[*] python3 Hash-Cracker.py -t <type> -h <hash> -w <wordlist>")
        sys.exit(1)

    # require wordlist unless -n enabled
    if not numbersBruteForce and not wordlist:
        print("[-] You must provide a wordlist using -w (unless using -n)")
        sys.exit(1)

    # check SavedHashes.txt first
    try:
        with open("SavedHashes.txt", "a+", encoding="utf-8") as f:
            f.seek(0)
            for solvedHash in f:
                parts = solvedHash.split(":")
                if len(parts) >= 2:
                    saved_key = parts[0].strip()
                    saved_hash = parts[1].strip().lower()
                    if userHash.strip().lower() == saved_hash:
                        print(f"[*] Saved Hash is: {saved_key}")
                        sys.exit(0)
    except Exception:
        # If SavedHashes.txt can't be opened for some reason, ignore and continue
        pass

    print(f"[*] Hash: {userHash}")
    print(f"[*] Hash type: {hashType}")
    if numbersBruteForce:
        print("[*] Mode: Numbers brute-force")
    else:
        print(f"[*] Wordlist: {wordlist}")
    print("[+] Cracking...")

    h = HashCracking()
    try:
        h.hashCrackWordlist(userHash, hashType, wordlist, verbose, bruteForce=numbersBruteForce)
    except KeyboardInterrupt:
        print("\n[Exiting...]")
        print(f"Words tried: {h.lineCount}")


if __name__ == "__main__":
    main(sys.argv[1:])

