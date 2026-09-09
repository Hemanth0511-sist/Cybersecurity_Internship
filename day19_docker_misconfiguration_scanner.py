def analyze_dockerfile(path):
    print("=" * 70)
    print("       DAY 19 - DOCKER CONTAINER MISCONFIGURATION SCANNER")
    print("=" * 70)

    print("\nAuthorized defensive training environment.")
    print("Analyzing a local mock Dockerfile only.")

    print("\nDockerfile Analysis")
    print("-" * 70)
    print(f"Target file : {path}")

    has_explicit_user = False
    risks = []

    try:
        with open(path, "r") as file:
            lines = file.readlines()

        for idx, line in enumerate(lines, 1):
            cleaned = line.strip().upper()

            if not cleaned or cleaned.startswith("#"):
                continue

            print(f"Line {idx:<3}: {line.strip()}")

            # Check for explicit USER configuration
            if cleaned.startswith("USER"):
                has_explicit_user = True

            # Check for unpinned latest image
            if cleaned.startswith("FROM") and ":LATEST" in cleaned:
                risks.append(
                    f"Line {idx}: Unpinned 'latest' image tag detected"
                )

            # Check for SSH port exposure
            if "EXPOSE 22" in cleaned:
                risks.append(
                    f"Line {idx}: SSH port 22 exposed"
                )

        # Check whether a USER directive exists
        if not has_explicit_user:
            risks.append(
                "No explicit USER directive detected"
            )

        print("\nSecurity Findings")
        print("-" * 70)

        if risks:
            for risk in risks:
                print(f"[RISK DETECTED] {risk}")
        else:
            print("[PASS] No major configuration risks detected.")

        print("\nSecurity Summary")
        print("-" * 70)
        print(f"Configuration lines analyzed : {len(lines)}")
        print(f"Security risks detected      : {len(risks)}")

        if risks:
            print("Overall status               : REVIEW REQUIRED")
        else:
            print("Overall status               : GOOD")

        print("\nRecommended Defensive Actions")
        print("-" * 70)
        print("[1] Pin container images to a specific version.")
        print("[2] Use a dedicated non-root application user.")
        print("[3] Avoid exposing unnecessary administrative services.")
        print("[4] Review container configuration before deployment.")

    except FileNotFoundError:
        print(f"[ERROR] Dockerfile not found: {path}")

    print("\n" + "=" * 70)
    print("             ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    analyze_dockerfile("day19_mock_Dockerfile")