def isolate_compromised_host(host_ip):
    print("=" * 70)
    print("       DAY 29 - INCIDENT CONTAINMENT & ASSET ISOLATION")
    print("=" * 70)

    print("\nAuthorized defensive training environment.")
    print("Simulating incident containment locally.")
    print(f"Target asset : {host_ip}")

    print("\nContainment Protocol")
    print("-" * 70)

    print("[SIMULATED] Step 1: Revoking active sessions...")
    print("[SIMULATED] Step 2: Applying QUARANTINE security controls...")
    print("[SIMULATED] Step 3: Restricting external network access...")

    print("\n[+] CONTAINMENT SUCCESSFUL")
    print(f"[+] Asset {host_ip} is marked for isolation.")

    print("\nImportant Safety Check")
    print("-" * 70)
    print("[1] No real network isolation performed.")
    print("[2] No firewall configuration changed.")
    print("[3] No active sessions were terminated.")
    print("[4] Simulation completed using a test asset identifier.")


def main():
    test_host = "192.0.2.150"

    isolate_compromised_host(test_host)

    print("\nIncident Response Playbook Overview")
    print("-" * 70)
    print("[1] Identify the affected asset.")
    print("[2] Confirm the security incident.")
    print("[3] Initiate containment procedures.")
    print("[4] Preserve relevant security evidence.")
    print("[5] Escalate to the incident-response team.")
    print("[6] Remediate the affected system.")
    print("[7] Validate recovery before returning to service.")

    print("\n" + "=" * 70)
    print("          INCIDENT CONTAINMENT SIMULATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()