import whois
import socket
import requests


def osint_scan(domain):
    print("=" * 50)
    print("        OSINT PASSIVE RECONNAISSANCE")
    print("=" * 50)

    print(f"\nTarget Domain : {domain}")

    # DNS / IP Resolution
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address    : {ip}")
    except socket.gaierror:
        print("IP Address    : Unable to resolve")
        ip = None

    # WHOIS Information
    try:
        w = whois.whois(domain)

        print("\n--- WHOIS INFORMATION ---")
        print(f"Registrar     : {w.registrar}")
        print(f"Creation Date : {w.creation_date}")
        print(f"Expiration    : {w.expiration_date}")
        print(f"Name Servers  : {w.name_servers}")

    except Exception as e:
        print("\nWHOIS information could not be retrieved.")
        print(f"Reason        : {e}")

    # IP Geolocation
    if ip:
        try:
            response = requests.get(
                f"http://ip-api.com/json/{ip}",
                timeout=10
            )
            geo = response.json()

            print("\n--- IP GEOLOCATION ---")

            if geo.get("status") == "success":
                print(f"Country       : {geo.get('country')}")
                print(f"Region        : {geo.get('regionName')}")
                print(f"City          : {geo.get('city')}")
                print(f"ISP           : {geo.get('isp')}")
                print(f"Organization  : {geo.get('org')}")
            else:
                print("Geolocation information unavailable.")

        except requests.RequestException as e:
            print("\nGeolocation request failed.")
            print(f"Reason        : {e}")

    print("\n" + "=" * 50)
    print("             SCAN COMPLETED")
    print("=" * 50)


# Authorized practice domain
osint_scan("example.com")