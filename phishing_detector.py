def check_phishing(email_text):
    # 1. Define our "Red Flag" keywords
    red_flags = ["urgent", "action required", "verify your account", "password reset", "suspended", "immediately", "bank"]
    
    # 2. Convert text to lowercase so we don't miss "URGENT" or "Urgent"
    email_content = email_text.lower()
    
    score = 0
    found_flags = []

    # 3. Check for keywords
    for flag in red_flags:
        if flag in email_content:
            score += 1
            found_flags.append(flag)

    # 4. Check for suspicious links (simplified)
    if "http://" in email_content:
        score += 2
        found_flags.append("Insecure Link (http)")

    # 5. Display the results
    print("--- Phishing Analysis Report ---")
    if score >= 3:
        print(f"[DANGER] Highly likely to be PHISHING! Score: {score}")
        print(f"[!] Red flags found: {found_flags}")
    elif score > 0:
        print(f"[WARNING] Suspicious email. Score: {score}")
        print(f"[!] Flags found: {found_flags}")
    else:
        print("[SAFE] No obvious phishing indicators found.")

# --- TESTING ---
test_email = """
Subject: URGENT: Your bank account has been suspended!
Dear customer, please click http://fakebank-login.com to verify your account immediately.
"""

check_phishing(test_email)
