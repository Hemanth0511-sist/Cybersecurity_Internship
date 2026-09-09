import os


MAGIC_SIGNATURES = {
    "PNG": b"\x89PNG\r\n\x1a\n",
    "JPEG": b"\xff\xd8\xff",
    "PDF": b"%PDF",
    "ZIP": b"PK\x03\x04"
}


ALLOWED_EXTENSIONS = {
    ".png": "PNG",
    ".jpg": "JPEG",
    ".jpeg": "JPEG",
    ".pdf": "PDF"
}


def detect_file_type(file_path):
    try:
        with open(file_path, "rb") as file:
            header = file.read(8)

        for file_type, signature in MAGIC_SIGNATURES.items():
            if header.startswith(signature):
                return file_type

        return "UNKNOWN"

    except OSError:
        return "UNREADABLE"


def validate_upload(file_path):
    filename = os.path.basename(file_path)
    extension = os.path.splitext(filename)[1].lower()

    detected_type = detect_file_type(file_path)

    print(f"\nFile: {filename}")
    print(f"Extension      : {extension or '<none>'}")
    print(f"Magic bytes    : {detected_type}")

    if extension not in ALLOWED_EXTENSIONS:
        print("[REJECTED] File extension is not allowed.")
        return False

    expected_type = ALLOWED_EXTENSIONS[extension]

    if detected_type != expected_type:
        print(
            f"[REJECTED] File signature does not match "
            f"the expected {expected_type} format."
        )
        return False

    print("[ACCEPTED] Extension and magic bytes match.")
    return True


def create_test_files():
    files = {
        "safe_image.png": MAGIC_SIGNATURES["PNG"] + b"SAFE-PNG-DATA",
        "safe_document.pdf": MAGIC_SIGNATURES["PDF"] + b"SAFE-PDF-DATA",
        "fake_image.png": b"NOT-A-PNG-FILE",
        "unknown_file.exe": b"MZ-SIMULATED-DATA"
    }

    for filename, content in files.items():
        with open(filename, "wb") as file:
            file.write(content)


def main():
    print("=" * 70)
    print("       DAY 25 - FILE UPLOAD MAGIC BYTES VALIDATOR")
    print("=" * 70)

    print("\nAuthorized defensive training environment.")
    print("Testing synthetic files locally.")

    create_test_files()

    test_files = [
        "safe_image.png",
        "safe_document.pdf",
        "fake_image.png",
        "unknown_file.exe"
    ]

    accepted = 0
    rejected = 0

    print("\nFile Validation Results")
    print("-" * 70)

    for file_path in test_files:
        if validate_upload(file_path):
            accepted += 1
        else:
            rejected += 1

    print("\n" + "=" * 70)
    print("             VALIDATION SUMMARY")
    print("=" * 70)

    print(f"Files tested       : {len(test_files)}")
    print(f"Files accepted     : {accepted}")
    print(f"Files rejected     : {rejected}")

    print("\nSecurity Checks")
    print("-" * 70)
    print("[1] File extension checked.")
    print("[2] File magic bytes inspected.")
    print("[3] Extension/signature mismatch detected.")
    print("[4] Unsupported file types rejected.")
    print("[5] Validation performed locally.")

    print("\n" + "=" * 70)
    print("          FILE UPLOAD VALIDATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()