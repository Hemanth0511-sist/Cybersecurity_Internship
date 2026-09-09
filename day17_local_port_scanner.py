import socket


HOST = "127.0.0.1"

PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    5432: "PostgreSQL",
    8080: "Web/Development Service"
}


def scan_local_ports(host, ports):
    print("=" * 65)
    print("       DAY 17 - LOCAL NETWORK PORT & SERVICE SCANNING")
    print("=" * 65)

    print("\nAuthorized defensive training environment.")
    print("Target: localhost only")
    print(f"Host  : {host}")

    print("\nScanning selected local ports...")
    print("-" * 65)

    open_services = []
    closed_ports = []

    for port in ports:
        service = PORTS.get(port, "Unknown")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)

        try:
            result = sock.connect_ex((host, port))

            if result == 0:
                print(
                    f"[OPEN]   Port {port:<5} | "
                    f"Service: {service}"
                )
                open_services.append((port, service))
            else:
                print(
                    f"[CLOSED] Port {port:<5} | "
                    f"Service: {service}"
                )
                closed_ports.append((port, service))

        except socket.error as error:
            print(
                f"[ERROR]  Port {port:<5} | "
                f"Service: {service} | {error}"
            )

        finally:
            sock.close()

    print("\n" + "=" * 65)
    print("             NETWORK EXPOSURE SUMMARY")
    print("=" * 65)

    print(f"Ports checked : {len(ports)}")
    print(f"Open ports   : {len(open_services)}")
    print(f"Closed ports : {len(closed_ports)}")

    if open_services:
        print("\nExposed Local Services")
        print("-" * 65)

        for port, service in open_services:
            print(f"Port {port:<5} -> {service}")

    else:
        print("\nNo open services detected in the selected ports.")

    print("\nSecurity Observation")
    print("-" * 65)

    if open_services:
        print(
            "Open services were detected on localhost. "
            "Only required development services should remain enabled."
        )
    else:
        print(
            "No exposed services were detected in the selected "
            "localhost ports."
        )

    print("\n" + "=" * 65)
    print("             SCAN COMPLETE")
    print("=" * 65)


if __name__ == "__main__":
    scan_local_ports(HOST, PORTS)