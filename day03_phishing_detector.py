import re
from urllib.parse import urlparse


KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "bank",
    "paypal"
]


def phish_score(url):
    parsed = urlparse(url)
    score = 0
    reasons = []

    # Check HTTPS
    if parsed.scheme != "https":
        score += 30
        reasons.append("Not using HTTPS")

    # Check suspicious keywords in hostname
    hostname = parsed.netloc.lower()

    for keyword in KEYWORDS:
        if keyword in hostname:
            score += 20
            reasons.append(f"Suspicious keyword: {keyword}")

    # Check excessive subdomains
    if hostname.count(".") > 3:
        score += 25
        reasons.append("Excessive number of subdomains")

    # Check whether hostname is an IPv4 address
    if re.fullmatch(
        r"\d{1,3}(\.\d{1,3}){3}",
        hostname
    ):
        score += 40
        reasons.append("URL uses an IP address")

    score = min(score, 100)

    if score >= 70:
        risk = "HIGH"
    elif score >= 40:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return score, risk, reasons


# 10 sample URLs for analysis
urls = [
    "https://github.com",
    "https://www.microsoft.com",
    "https://example.com",
    "http://example.com",
    "https://paypal-login.evil.com/verify",
    "http://secure-account.example.com/login",
    "https://login.verify.account.example.com",
    "http://192.0.2.10/login",
    "https://bank-update.example.com",
    "http://account-security.example.com/verify"
]


print("=" * 65)
print("             PHISHING URL DETECTION LAB")
print("=" * 65)

for number, url in enumerate(urls, 1):

    score, risk, reasons = phish_score(url)

    print(f"\n[{number}] {url}")
    print(f"Risk Score : {score}%")
    print(f"Risk Level : {risk}")

    if reasons:
        print("Indicators  :")
        for reason in reasons:
            print(f"  - {reason}")
    else:
        print("Indicators  : No suspicious indicators detected")

print("\n" + "=" * 65)
print("                    ANALYSIS COMPLETE")
print("=" * 65)