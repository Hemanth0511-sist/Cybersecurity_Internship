import re
from collections import Counter


LOG_SAMPLE = """
2026-08-21 02:34:12 FAILED_LOGIN user=admin ip=45.33.32.156
2026-08-21 02:34:14 FAILED_LOGIN user=admin ip=45.33.32.156
2026-08-21 02:34:16 FAILED_LOGIN user=admin ip=45.33.32.156
2026-08-21 02:34:20 SUCCESS_LOGIN user=admin ip=45.33.32.156
2026-08-21 08:00:01 SUCCESS_LOGIN user=student ip=192.168.1.10
2026-08-21 02:35:00 EMAIL_RULE_CREATED user=admin rule=forward_all
2026-08-21 09:15:00 SUCCESS_LOGIN user=student ip=192.168.1.10
"""


def analyze_logs(logs):

    print("\n" + "=" * 65)
    print("             SIEM LOG ANALYSIS REPORT")
    print("=" * 65)

    # Find failed login events
    failed_logins = re.findall(
        r'FAILED_LOGIN user=(\w+) ip=([\d.]+)',
        logs
    )

    # Find suspicious email-rule creation
    email_rules = re.findall(
        r'EMAIL_RULE_CREATED user=(\w+) rule=(\S+)',
        logs
    )

    # Count failed logins per user
    fail_counts = Counter(
        user for user, ip in failed_logins
    )

    print("\n--- FAILED LOGIN ANALYSIS ---")

    if not fail_counts:
        print("No failed login events detected.")
    else:
        for user, count in fail_counts.items():

            print(f"User: {user}")
            print(f"Failed attempts: {count}")

            if count >= 3:
                print(
                    f"[ALERT] Possible brute-force activity: "
                    f"{user} ({count} failures)"
                )
            else:
                print("[INFO] Below alert threshold.")

    print("\n--- EMAIL RULE ANALYSIS ---")

    if not email_rules:
        print("No email-rule creation events detected.")
    else:
        for user, rule in email_rules:

            print(f"User: {user}")
            print(f"Rule : {rule}")

            print(
                f"[ALERT] Suspicious email rule created by: {user}"
            )

    print("\n--- SECURITY SUMMARY ---")

    alerts = 0

    for user, count in fail_counts.items():
        if count >= 3:
            alerts += 1

    alerts += len(email_rules)

    print(f"Failed-login users analyzed : {len(fail_counts)}")
    print(f"Email-rule events analyzed  : {len(email_rules)}")
    print(f"Security alerts generated   : {alerts}")

    print("\n" + "=" * 65)
    print("                 ANALYSIS COMPLETE")
    print("=" * 65)


print("=" * 65)
print("       DAY 13 - SIEM LOG ANALYSIS LAB")
print("=" * 65)

print("\nAnalyzing sample security logs...")

analyze_logs(LOG_SAMPLE)