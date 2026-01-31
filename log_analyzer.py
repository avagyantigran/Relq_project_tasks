def analyze_logs(file_path):
    failed_attempts = {} # A dictionary to keep track of IPs and counts

    try:
        with open(file_path, "r") as file:
            for line in file:
                # Check if the line contains a failure message
                if "FAILED LOGIN" in line:
                    # Split the line to get the IP (the first part of the line)
                    ip = line.split(" ")[0]
                    
                    # Add to our count
                    if ip in failed_attempts:
                        failed_attempts[ip] += 1
                    else:
                        failed_attempts[ip] = 1

        print("--- SECURITY REPORT ---")
        for ip, count in failed_attempts.items():
            if count > 3:
                print(f"[ALERT] Possible Brute Force: {ip} failed {count} times!")
            else:
                print(f"[INFO] {ip} had {count} failed attempts.")

    except FileNotFoundError:
        print("[-] Error: Log file not found.")

# Run it on our test file
analyze_logs("server_log.txt")
