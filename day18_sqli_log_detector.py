import re


MOCK_ACCESS_LOGS = [
    '192.168.1.45 - "GET /profile?id=5 HTTP/1.1" 200',
    '10.0.4.12 - "POST /auth/login?user=admin%27%20OR%20%271%27=%271 HTTP/1.1" 401',
    '172.16.5.9 - "GET /search?q=UNION%20SELECT%20null,password%20FROM%20users-- HTTP/1.1" 500',
    '192.168.1.50 - "GET /products?id=12 HTTP/1.1" 200',
    '10.0.4.25 - "GET /home HTTP/1.1" 200',
    '172.16.5.20 - "GET /search?q=normal%20security%20query HTTP/1.1" 200'
]


def analyze_sqli_signatures(logs):
    print("=" * 70)
    print("       DAY 18 - SQL INJECTION LOG DETECTION ENGINE")
    print("=" * 70)

    print("\nAuthorized defensive training environment.")
    print("Analyzing mock web access logs only.")

    print("\nSQL Injection Detection")
    print("-" * 70)

    sqli_regex = re.compile(
        r"(?i)('|--|#|UNION\s+SELECT|OR\s+\d+=\d+)"
    )

    total_logs = len(logs)
    suspicious = 0
    normal = 0

    for entry in logs:
        if sqli_regex.search(entry):
            source_ip = entry.split(" ")[0]

            suspicious += 1

            print("[CRITICAL MALICIOUS PATTERN]")
            print(f"Source IP : {source_ip}")
            print(f"Log Entry : {entry}")
            print()

        else:
            normal += 1

    print("=" * 70)
    print("             LOG ANALYSIS SUMMARY")
    print("=" * 70)

    print(f"Total log entries analyzed : {total_logs}")
    print(f"Suspicious entries         : {suspicious}")
    print(f"Normal entries             : {normal}")

    if suspicious > 0:
        print("\nSecurity Status             : ALERT")
        print(
            "Potential SQL injection patterns were detected "
            "in the mock access logs."
        )
    else:
        print("\nSecurity Status             : CLEAN")
        print("No SQL injection patterns were detected.")

    print("\nDetection Patterns")
    print("-" * 70)
    print("1. Single quote patterns")
    print("2. SQL comment markers")
    print("3. UNION SELECT")
    print("4. OR numeric comparison patterns")

    print("\n" + "=" * 70)
    print("             ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    analyze_sqli_signatures(MOCK_ACCESS_LOGS)