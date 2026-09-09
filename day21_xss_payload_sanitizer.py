import html
import re


def sanitize_user_input(raw_payload):
    # Encode HTML-sensitive characters
    encoded_string = html.escape(raw_payload)

    # Neutralize common active XSS tokens
    sanitized = re.sub(
        r"(?i)script|onerror|onload|javascript:",
        "[PROHIBITED_TOKEN]",
        encoded_string
    )

    return sanitized


test_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "<body onload=alert(1)>",
    "javascript:alert(1)",
    "<script>document.cookie</script>",
    "<div onerror=alert(1)>Test</div>",
    "<svg onload=alert(1)>",
    "<script src='test.js'></script>",
    "<a href='javascript:alert(1)'>Click</a>",
    "<input onload=alert(1)>"
]


print("=" * 70)
print("       DAY 21 - XSS PAYLOAD SANITIZER")
print("=" * 70)

print("\nAuthorized defensive training environment.")
print("Testing simulated XSS inputs locally only.")

print("\nXSS Sanitization Results")
print("-" * 70)

for number, payload in enumerate(test_payloads, 1):
    sanitized = sanitize_user_input(payload)

    print(f"\nTest {number}")
    print(f"Raw Input       : {payload}")
    print(f"Neutralized     : {sanitized}")

print("\n" + "=" * 70)
print("             SECURITY SUMMARY")
print("=" * 70)

print(f"Test parameters analyzed : {len(test_payloads)}")
print("Input encoding           : ENABLED")
print("Active token filtering   : ENABLED")
print("Overall status           : DEFENSIVE SANITIZATION COMPLETE")

print("\nProtection Approach")
print("-" * 70)
print("[1] HTML-sensitive characters are encoded.")
print("[2] Common active XSS tokens are neutralized.")
print("[3] User input is treated as untrusted data.")
print("[4] Output should be contextually encoded before rendering.")

print("\n" + "=" * 70)
print("             SANITIZATION COMPLETE")
print("=" * 70)