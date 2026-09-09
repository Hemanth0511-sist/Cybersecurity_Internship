import ipaddress


def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def process_threat_intelligence(feed):
    print("=" * 70)
    print("       DAY 24 - AUTOMATED THREAT INTEL IP BLOCKING")
    print("=" * 70)

    print("\nAuthorized defensive training environment.")
    print("Processing simulated threat-intelligence indicators locally.")

    print("\nThreat Intelligence Feed")
    print("-" * 70)

    blocklist = set()
    invalid_entries = []

    for entry in feed:
        ip = entry["ip"]
        threat_type = entry["threat"]
        confidence = entry["confidence"]

        if not validate_ip(ip):
            invalid_entries.append(ip)
            print(f"[REJECTED] Invalid IP indicator: {ip}")
            continue

        blocklist.add(ip)

        print(
            f"[BLOCK] {ip:<15} | "
            f"Threat: {threat_type:<18} | "
            f"Confidence: {confidence}%"
        )

    print("\n" + "=" * 70)
    print("             PIPELINE SUMMARY")
    print("=" * 70)

    print(f"Indicators received : {len(feed)}")
    print(f"Valid indicators    : {len(blocklist)}")
    print(f"Invalid indicators  : {len(invalid_entries)}")
    print(f"Local blocklist     : {len(blocklist)}")

    print("\nLocal Defensive Blocklist")
    print("-" * 70)

    for ip in sorted(blocklist):
        print(f"[BLOCKED] {ip}")

    print("\nValidation Checks")
    print("-" * 70)
    print("[1] Threat indicators validated.")
    print("[2] Invalid indicators rejected.")
    print("[3] Valid indicators added to local blocklist.")
    print("[4] No external firewall changes performed.")
    print("[5] Pipeline completed in simulation mode.")

    print("\n" + "=" * 70)
    print("       THREAT INTELLIGENCE PIPELINE COMPLETE")
    print("=" * 70)


def main():
    mock_feed = [
        {
            "ip": "203.0.113.10",
            "threat": "Malware C2",
            "confidence": 95
        },
        {
            "ip": "198.51.100.25",
            "threat": "Phishing",
            "confidence": 90
        },
        {
            "ip": "192.0.2.44",
            "threat": "Botnet",
            "confidence": 88
        },
        {
            "ip": "invalid-ip",
            "threat": "Unknown",
            "confidence": 40
        }
    ]

    process_threat_intelligence(mock_feed)


if __name__ == "__main__":
    main()