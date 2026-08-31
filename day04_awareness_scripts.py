def generate_awareness_script(target_type, pretext, trigger):
    script = f"""
============================================================
          SOCIAL ENGINEERING AWARENESS SIMULATION
============================================================

Scenario Type : {target_type}
Pretext       : {pretext}
Psychological Trigger : {trigger}

--- SIMULATED MESSAGE ---

"This is a SECURITY AWARENESS TRAINING exercise.

The caller/message may create a sense of urgency and authority
to make the recipient act quickly.

IMPORTANT:
Do NOT provide passwords, OTPs, PINs, banking details,
security codes, or other sensitive information.

Instead:
1. End the conversation if you feel pressured.
2. Contact the organization through its official channel.
3. Verify the request independently.
4. Report suspicious activity to the appropriate team.

--- RED FLAGS ---

* Unexpected contact
* Urgency or pressure
* Request for confidential information
* Unusual instructions
* Request to bypass normal procedures

--- DEFENSIVE RESPONSE ---

"Thank you. I will verify this request through the
official contact method before taking any action."

============================================================
"""
    return script


scenarios = [
    {
        "type": "IT Support",
        "pretext": "Urgent account-security notification",
        "trigger": "Authority + urgency"
    },
    {
        "type": "Banking",
        "pretext": "Suspicious transaction notification",
        "trigger": "Fear + urgency"
    },
    {
        "type": "Government Service",
        "pretext": "Important account verification notice",
        "trigger": "Authority + fear"
    }
]


print("=" * 60)
print("       DAY 4 - VISHING & SMISHING AWARENESS LAB")
print("=" * 60)

for i, scenario in enumerate(scenarios, 1):
    print(f"\nSCENARIO {i}")
    print(
        generate_awareness_script(
            scenario["type"],
            scenario["pretext"],
            scenario["trigger"]
        )
    )

print("=" * 60)
print("                 SIMULATION COMPLETE")
print("=" * 60)