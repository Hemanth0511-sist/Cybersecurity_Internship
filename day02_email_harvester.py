import re
import requests


def harvest_emails(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        html = response.text

        emails = set(
            re.findall(
                r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}',
                html
            )
        )

        return emails

    except requests.RequestException as e:
        print(f"Error accessing website: {e}")
        return set()


# Authorized lab/practice page
url = "http://localhost:8000/lab_page.html"

found = harvest_emails(url)

print("=" * 50)
print("       EMAIL HARVESTING - LAB DEMO")
print("=" * 50)

print(f"\nURL: {url}")
print(f"Emails found: {len(found)}")

if found:
    print("\n--- EMAIL ADDRESSES ---")
    for email in sorted(found):
        print(email)
else:
    print("\nNo email addresses found.")

print("\n" + "=" * 50)