def generate_awareness_email(target):
    return f"""
============================================================
        PHISHING AWARENESS TRAINING - LAB SIMULATION
============================================================

TRAINING ONLY - DO NOT SEND TO REAL USERS

From    : SECURITY-AWARENESS@LAB.LOCAL
To      : {target["email"]}
Subject : Security Awareness Exercise - Account Verification

Hi {target["name"]},

This is a controlled cybersecurity awareness exercise.

A simulated security notification may create urgency and
encourage the recipient to verify an account quickly.

IMPORTANT:
Do NOT enter passwords, OTPs, PINs, banking information,
or other confidential information into unexpected forms.

TRAINING LINK:
https://training.invalid/awareness-test

The .invalid domain is intentionally non-functional and is
used only as a safe training placeholder.

------------------------------------------------------------
PHISHING RED FLAGS
------------------------------------------------------------

1. Unexpected security notification
2. Pressure to act quickly
3. Personalized information used to create trust
4. Request to verify an account
5. Suspicious or unfamiliar link

------------------------------------------------------------
DEFENSIVE RESPONSE
------------------------------------------------------------

Verify the request through the organization's official
website or known contact method.

Never rely solely on links or contact information provided
inside an unexpected message.

------------------------------------------------------------
EMAIL AUTHENTICATION
------------------------------------------------------------

SPF  - Helps authorize which mail servers can send mail
       for a domain.

DKIM - Uses cryptographic signatures to help verify that
       an email was authorized and not modified.

DMARC - Helps domain owners define how receiving systems
        should handle messages that fail authentication.

============================================================
             END OF AWARENESS SIMULATION
============================================================
"""


targets = [
    {
        "name": "Training User 1",
        "email": "user1@lab.example",
        "company": "Lab Organization"
    },
    {
        "name": "Training User 2",
        "email": "user2@lab.example",
        "company": "Lab Organization"
    },
    {
        "name": "Training User 3",
        "email": "user3@lab.example",
        "company": "Lab Organization"
    }
]


print("=" * 60)
print("       DAY 6 - PHISHING AWARENESS LAB")
print("=" * 60)

for number, target in enumerate(targets, 1):
    print(f"\nTRAINING EMAIL {number}")
    print(generate_awareness_email(target))

print("=" * 60)
print("             SIMULATION COMPLETE")
print("=" * 60)