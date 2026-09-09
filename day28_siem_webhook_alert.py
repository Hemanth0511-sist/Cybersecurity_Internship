import json


def process_siem_alert(alert):
    print("\nSIEM Alert Received")
    print("-" * 70)

    print(f"Alert ID   : {alert['alert_id']}")
    print(f"Severity   : {alert['severity']}")
    print(f"Source IP  : {alert['source_ip']}")
    print(f"Event      : {alert['event']}")

    if alert["severity"] in ["CRITICAL", "HIGH"]:
        return True

    return False


def simulate_webhook(alert):
    payload = {
        "alert_id": alert["alert_id"],
        "severity": alert["severity"],
        "source_ip": alert["source_ip"],
        "event": alert["event"],
        "action": "SECURITY_ALERT_TRIGGERED"
    }

    print("\nWebhook Payload")
    print("-" * 70)
    print(json.dumps(payload, indent=2))

    print("\n[SIMULATED WEBHOOK]")
    print("[+] Alert notification would be sent to the configured")
    print("    security communication channel.")
    print("[+] No external webhook request was performed.")


def main():
    print("=" * 70)
    print("       DAY 28 - SIEM ALERT TRIGGER AUTOMATION")
    print("=" * 70)

    print("\nAuthorized defensive training environment.")
    print("Processing synthetic SIEM alerts locally.")

    alerts = [
        {
            "alert_id": "SIEM-001",
            "severity": "LOW",
            "source_ip": "192.0.2.10",
            "event": "Normal authentication"
        },
        {
            "alert_id": "SIEM-002",
            "severity": "HIGH",
            "source_ip": "198.51.100.20",
            "event": "Multiple failed authentication attempts"
        },
        {
            "alert_id": "SIEM-003",
            "severity": "CRITICAL",
            "source_ip": "203.0.113.50",
            "event": "Suspicious security event detected"
        },
        {
            "alert_id": "SIEM-004",
            "severity": "MEDIUM",
            "source_ip": "192.0.2.25",
            "event": "Unusual application activity"
        }
    ]

    triggered = 0
    ignored = 0

    for alert in alerts:
        should_trigger = process_siem_alert(alert)

        if should_trigger:
            triggered += 1
            simulate_webhook(alert)
        else:
            ignored += 1
            print("\n[INFO] No webhook action required for this severity.")

    print("\n" + "=" * 70)
    print("                 SIEM AUTOMATION SUMMARY")
    print("=" * 70)

    print(f"Alerts processed    : {len(alerts)}")
    print(f"Webhook triggers    : {triggered}")
    print(f"Alerts not triggered: {ignored}")

    print("\nSecurity Controls")
    print("-" * 70)
    print("[1] SIEM alerts evaluated by severity.")
    print("[2] HIGH and CRITICAL alerts trigger notification logic.")
    print("[3] Webhook payload generated locally.")
    print("[4] Lower-severity alerts do not trigger notification.")
    print("[5] No external webhook request was performed.")

    print("\n" + "=" * 70)
    print("            SIEM WEBHOOK SIMULATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()