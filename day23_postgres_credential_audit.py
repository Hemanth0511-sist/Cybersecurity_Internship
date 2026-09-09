def audit_credentials(target, credentials):
    print("=" * 70)
    print("       DAY 23 - POSTGRES DATABASE CREDENTIAL AUDITING")
    print("=" * 70)

    print("\nAuthorized defensive training environment.")
    print("Simulated PostgreSQL credential security audit.")
    print(f"Audit target : {target}")

    print("\nCredential Audit")
    print("-" * 70)

    critical_findings = 0
    reviewed = 0

    dangerous_pairs = {
        ("postgres", "postgres"),
        ("admin", "admin"),
        ("postgres", ""),
        ("admin", "")
    }

    for username, password in credentials.items():
        reviewed += 1

        if (username, password) in dangerous_pairs:
            critical_findings += 1
            display_password = password if password else "<BLANK>"

            print(
                f"[CRITICAL] Default/weak credential detected: "
                f"{username}:{display_password}"
            )
        else:
            masked = password[:3] + "***" if password else "<BLANK>"
            print(
                f"[PASS] Configuration pair reviewed -> "
                f"{username}:{masked}"
            )

    print("\n" + "=" * 70)
    print("             AUDIT SUMMARY")
    print("=" * 70)

    print(f"Credential pairs reviewed : {reviewed}")
    print(f"Critical findings         : {critical_findings}")

    if critical_findings == 0:
        print("Overall status            : PASS")
        print("No default credentials detected.")
    else:
        print("Overall status            : REVIEW REQUIRED")
        print("Default or weak credentials require remediation.")

    print("\nRecommended Controls")
    print("-" * 70)
    print("[1] Disable default database credentials.")
    print("[2] Enforce strong authentication policies.")
    print("[3] Limit database connection sources.")
    print("[4] Apply least-privilege database accounts.")
    print("[5] Protect sensitive database information.")

    print("\n" + "=" * 70)
    print("             AUDIT COMPLETE")
    print("=" * 70)


def main():
    credentials = {
        "postgres": "postgres",
        "app_user": "SecureP@ss2026!",
        "report_user": "Report#2026!"
    }

    audit_credentials("127.0.0.1", credentials)


if __name__ == "__main__":
    main()