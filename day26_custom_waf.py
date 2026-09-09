import re


WAF_RULES = [
    {
        "name": "SQL Injection Pattern",
        "pattern": r"(?i)(union\s+select|or\s+1\s*=\s*1|drop\s+table)"
    },
    {
        "name": "XSS Pattern",
        "pattern": r"(?i)(<script|javascript:|onerror\s*=|onload\s*=)"
    },
    {
        "name": "Path Traversal Pattern",
        "pattern": r"(\.\./|\.\.\\)"
    },
    {
        "name": "Command Injection Pattern",
        "pattern": r"(?i)(;\s*(whoami|ipconfig|dir)|\|\s*(whoami|ipconfig|dir))"
    }
]


def inspect_request(request):
    matched_rules = []

    for rule in WAF_RULES:
        if re.search(rule["pattern"], request):
            matched_rules.append(rule["name"])

    return matched_rules


def main():
    print("=" * 70)
    print("             DAY 26 - CUSTOM WEB APPLICATION FIREWALL")
    print("=" * 70)

    print("\nAuthorized defensive training environment.")
    print("Inspecting synthetic HTTP request patterns locally.")

    requests = [
        ("REQ-001", "GET /home"),
        ("REQ-002", "GET /products?id=25"),
        ("REQ-003", "GET /search?q=union select username"),
        ("REQ-004", "GET /page?name=<script>alert(1)</script>"),
        ("REQ-005", "GET /download?file=../../config.txt"),
        ("REQ-006", "GET /status"),
        ("REQ-007", "GET /check?cmd=; whoami"),
        ("REQ-008", "POST /login username=test")
    ]

    allowed = 0
    blocked = 0

    print("\nWAF Inspection Results")
    print("-" * 70)

    for request_id, request in requests:
        matched_rules = inspect_request(request)

        if matched_rules:
            blocked += 1

            print(f"[BLOCKED] {request_id}")
            print(f"          Request : {request}")

            for rule in matched_rules:
                print(f"          Rule    : {rule}")
        else:
            allowed += 1

            print(f"[ALLOWED] {request_id}")
            print(f"          Request : {request}")

    print("\n" + "=" * 70)
    print("                 WAF SUMMARY")
    print("=" * 70)

    print(f"Requests inspected : {len(requests)}")
    print(f"Requests allowed   : {allowed}")
    print(f"Requests blocked   : {blocked}")
    print(f"WAF rules active   : {len(WAF_RULES)}")

    print("\nSecurity Controls")
    print("-" * 70)
    print("[1] SQL injection patterns inspected.")
    print("[2] XSS patterns inspected.")
    print("[3] Path traversal patterns inspected.")
    print("[4] Command injection patterns inspected.")
    print("[5] Suspicious requests blocked locally.")
    print("[6] No external traffic or firewall changes performed.")

    print("\n" + "=" * 70)
    print("              WAF SIMULATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()