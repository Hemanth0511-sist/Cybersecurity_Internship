import requests


def audit_directory_paths(base_url, wordlist):
    print("=" * 70)
    print("       DAY 20 - WEB DIRECTORY BRUTE-FORCE SIMULATION")
    print("=" * 70)

    print("\nAuthorized defensive training environment.")
    print("Target: localhost only")

    print("\nEndpoint Discovery")
    print("-" * 70)
    print(f"Base URL : {base_url}")

    matches = 0
    restricted = 0
    unreachable = 0

    for directory in wordlist:
        target_path = f"{base_url}/{directory}"

        try:
            response = requests.get(target_path, timeout=3)

            if response.status_code == 200:
                matches += 1
                print(
                    f"[MATCH DETECTED] Route accessible: "
                    f"{target_path} (Status: 200)"
                )

            elif response.status_code == 403:
                restricted += 1
                print(
                    f"[RESTRICTED ROUTE] Forbidden resource mapped: "
                    f"{target_path} (Status: 403)"
                )

            else:
                print(
                    f"[NOT FOUND] {target_path} "
                    f"(Status: {response.status_code})"
                )

        except requests.RequestException:
            unreachable += 1
            print(f"[UNREACHABLE] {target_path}")

    print("\n" + "=" * 70)
    print("             DISCOVERY SUMMARY")
    print("=" * 70)

    print(f"Paths tested       : {len(wordlist)}")
    print(f"Accessible routes  : {matches}")
    print(f"Restricted routes  : {restricted}")
    print(f"Unreachable paths  : {unreachable}")

    print("\nDefensive Recommendations")
    print("-" * 70)
    print("[1] Remove unnecessary administrative endpoints.")
    print("[2] Restrict sensitive files from web access.")
    print("[3] Apply authentication and authorization controls.")
    print("[4] Configure explicit routing and access controls.")
    print("[5] Prevent backup and configuration files from being exposed.")

    print("\n" + "=" * 70)
    print("             AUDIT COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    audit_directory_paths(
        "http://127.0.0.1:8080",
        [
            "admin",
            "dashboard",
            "api/v1",
            ".env",
            "backup.sql"
        ]
    )