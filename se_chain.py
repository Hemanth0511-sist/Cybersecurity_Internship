import re
import socket
import json
from datetime import datetime


# ============================================================
# DAY 15 - SOCIAL ENGINEERING ATTACK CHAIN SIMULATOR
# AUTHORIZED EDUCATIONAL LAB ONLY
# ============================================================

REPORT_FILE = "day15_final_report.json"


# ============================================================
# MODULE 1 - PASSIVE OSINT
# ============================================================

def osint_module():
    print("\n" + "=" * 65)
    print("             MODULE: PASSIVE OSINT")
    print("=" * 65)

    domain = input("Enter lab domain [example.com]: ").strip()

    if not domain:
        domain = "example.com"

    print(f"\nTarget Domain : {domain}")

    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address    : {ip}")
    except socket.gaierror:
        ip = "Unable to resolve"
        print(f"IP Address    : {ip}")

    print("\n[INFO] Passive DNS resolution completed.")
    print("[INFO] No active scanning performed.")

    return {
        "domain": domain,
        "ip": ip
    }


# ============================================================
# MODULE 2 - PROFILE BUILD
# SYNTHETIC TRAINING DATA ONLY
# ============================================================

def profile_module():
    print("\n" + "=" * 65)
    print("             MODULE: PROFILE BUILD")
    print("=" * 65)

    profile = {
        "username": "training_user",
        "account_age_days": 420,
        "public_posts": 85,
        "profile_type": "synthetic training profile",
        "data_source": "lab-generated data"
    }

    print("\nSynthetic Profile")
    print("-" * 65)

    for key, value in profile.items():
        print(f"{key:20}: {value}")

    print("\n[INFO] No real person's profile was collected.")

    return profile


# ============================================================
# MODULE 3 - PHISHING URL SCORER
# ============================================================

def phish_module():
    print("\n" + "=" * 65)
    print("             MODULE: PHISHING URL SCORER")
    print("=" * 65)

    url = input(
        "Enter a URL for defensive analysis "
        "[https://example.com]: "
    ).strip()

    if not url:
        url = "https://example.com"

    score = 0
    indicators = []

    suspicious_keywords = [
        "login",
        "verify",
        "account",
        "secure",
        "bank",
        "update"
    ]

    lower_url = url.lower()

    if not lower_url.startswith("https://"):
        score += 30
        indicators.append("Not using HTTPS")

    if re.match(r"https?://\d+\.\d+\.\d+\.\d+", lower_url):
        score += 40
        indicators.append("URL uses an IP address")

    for keyword in suspicious_keywords:
        if keyword in lower_url:
            score += 10
            indicators.append(
                f"Suspicious keyword: {keyword}"
            )

    # Limit the score to 100
    score = min(score, 100)

    if score >= 70:
        risk = "HIGH"
    elif score >= 40:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    print("\nPhishing Analysis")
    print("-" * 65)
    print(f"URL         : {url}")
    print(f"Risk Score  : {score}%")
    print(f"Risk Level  : {risk}")

    if indicators:
        print("Indicators:")
        for indicator in indicators:
            print(f"  - {indicator}")
    else:
        print("Indicators  : No suspicious indicators detected")

    return {
        "url": url,
        "risk_score": score,
        "risk_level": risk,
        "indicators": indicators
    }


# ============================================================
# MODULE 4 - SAFE AWARENESS TEMPLATE
# ============================================================

def template_module():
    print("\n" + "=" * 65)
    print("             MODULE: AWARENESS TEMPLATE")
    print("=" * 65)

    template = """
------------------------------------------------------------
SECURITY AWARENESS TRAINING SIMULATION
------------------------------------------------------------

Subject: Security Awareness Exercise

This is a controlled cybersecurity awareness exercise.

A suspicious message may attempt to create urgency and
encourage the recipient to verify an account.

IMPORTANT:

Do NOT provide passwords, OTPs, PINs, banking information,
or other confidential information.

DEFENSIVE RESPONSE:

1. Stop and do not respond immediately.
2. Verify the request through an official channel.
3. Do not trust links from unexpected messages.
4. Report suspicious activity through the approved process.

------------------------------------------------------------
TRAINING ONLY - DO NOT SEND TO REAL USERS
------------------------------------------------------------
"""

    print(template)

    return {
        "type": "security awareness simulation",
        "delivery": "disabled",
        "credential_collection": "disabled"
    }


# ============================================================
# MODULE 5 - INCIDENT RESPONSE
# ============================================================

def ir_module(phish_result):
    print("\n" + "=" * 65)
    print("             MODULE: INCIDENT RESPONSE")
    print("=" * 65)

    incident = {
        "type": "phishing awareness alert",
        "severity": (
            "HIGH"
            if phish_result["risk_score"] >= 70
            else "MEDIUM"
            if phish_result["risk_score"] >= 40
            else "LOW"
        ),
        "time": str(datetime.now())
    }

    print("\nIncident")
    print("-" * 65)
    print(f"Type     : {incident['type']}")
    print(f"Severity : {incident['severity']}")
    print(f"Time     : {incident['time']}")

    actions = [
        "Record the security alert",
        "Preserve relevant evidence",
        "Notify the appropriate security team",
        "Review affected accounts if applicable",
        "Remove suspicious email rules if unauthorized",
        "Monitor for additional suspicious activity",
        "Document lessons learned"
    ]

    print("\nRecommended Defensive Actions")

    for action in actions:
        print(f"  [x] {action}")

    return {
        "incident": incident,
        "actions": actions
    }


# ============================================================
# FINAL REPORT
# ============================================================

def save_report(results):
    report = {
        "project": "SE Attack Chain Simulator",
        "purpose": "Authorized cybersecurity education",
        "timestamp": str(datetime.now()),
        "modules": results
    }

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print(f"\nFinal report saved to: {REPORT_FILE}")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    print("=" * 65)
    print("        DAY 15 - SE ATTACK CHAIN SIMULATOR")
    print("=" * 65)
    print("       AUTHORIZED EDUCATIONAL LAB ONLY")
    print("=" * 65)

    print("""
Available Modules:

[1] OSINT    - Passive domain information
[2] Profile  - Synthetic profile analysis
[3] Phish    - Defensive URL risk scoring
[4] Template - Security awareness simulation
[5] IR       - Incident response workflow
[6] Full     - Run complete simulation
[0] Exit
""")

    results = {}

    choice = input("Select module: ").strip().lower()

    if choice == "1":
        results["osint"] = osint_module()

    elif choice == "2":
        results["profile"] = profile_module()

    elif choice == "3":
        results["phish"] = phish_module()

    elif choice == "4":
        results["template"] = template_module()

    elif choice == "5":
        sample_phish = {
            "risk_score": 70,
            "risk_level": "HIGH"
        }

        results["ir"] = ir_module(sample_phish)

    elif choice == "6":
        print("\nLaunching complete training simulation...")

        results["osint"] = osint_module()
        results["profile"] = profile_module()
        results["phish"] = phish_module()
        results["template"] = template_module()
        results["ir"] = ir_module(results["phish"])

    elif choice == "0":
        print("\nExiting simulator.")
        return

    else:
        print("\nInvalid choice.")
        return

    save_report(results)

    print("\n" + "=" * 65)
    print("             SIMULATION COMPLETE")
    print("=" * 65)


if __name__ == "__main__":
    main()