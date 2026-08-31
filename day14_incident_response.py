import json
import datetime


INCIDENT_FILE = "day14_incident_report.json"


def collect_incident_details():
    print("\n" + "=" * 65)
    print("          INCIDENT DETAILS")
    print("=" * 65)

    incident = {
        "incident_id": "SE-2026-001",
        "timestamp": str(datetime.datetime.now()),
        "type": input("Incident type: ").strip(),
        "reported_by": input("Reported by: ").strip(),
        "description": input("Description: ").strip(),
        "severity": input("Severity (LOW/MEDIUM/HIGH): ").strip().upper()
    }

    return incident


def response_plan(incident):
    print("\n" + "=" * 65)
    print("        SOCIAL ENGINEERING INCIDENT RESPONSE")
    print("=" * 65)

    phases = [
        (
            "1. IDENTIFY",
            [
                "Confirm the reported social-engineering incident.",
                "Identify affected accounts, users, devices, and messages.",
                "Preserve relevant evidence such as email headers and logs."
            ]
        ),
        (
            "2. CONTAIN",
            [
                "Restrict affected accounts if necessary.",
                "Block suspicious messages, domains, or indicators.",
                "Prevent further unauthorized access."
            ]
        ),
        (
            "3. ERADICATE",
            [
                "Remove malicious messages or unauthorized email rules.",
                "Reset affected credentials through approved procedures.",
                "Remove unauthorized software or persistence mechanisms."
            ]
        ),
        (
            "4. RECOVER",
            [
                "Restore affected services safely.",
                "Monitor accounts and systems for additional suspicious activity.",
                "Confirm normal operation before closing the incident."
            ]
        ),
        (
            "5. LESSONS LEARNED",
            [
                "Document what happened and how it was detected.",
                "Identify security-control weaknesses.",
                "Improve awareness training and preventive controls."
            ]
        )
    ]

    for phase, actions in phases:
        print(f"\n--- {phase} ---")

        for action in actions:
            print(f"[ ] {action}")


def save_report(incident):
    report = {
        "incident": incident,
        "response_status": "Response plan generated",
        "generated_at": str(datetime.datetime.now())
    }

    with open(INCIDENT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print(f"\nIncident report saved to: {INCIDENT_FILE}")


print("=" * 65)
print("       DAY 14 - INCIDENT RESPONSE LAB")
print("=" * 65)

print("\nAuthorized defensive training environment.")

incident = collect_incident_details()

response_plan(incident)

save_report(incident)

print("\n" + "=" * 65)
print("             INCIDENT RESPONSE COMPLETE")
print("=" * 65)