import platform
import socket
import datetime
import os


def usb_payload_sim(output_file="recon_log.txt"):
    system_info = {
        "timestamp": str(datetime.datetime.now()),
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "version": platform.version(),
        "user": os.getenv("USERNAME") or os.getenv("USER"),
        "working_directory": os.getcwd()
    }

    with open(output_file, "w", encoding="utf-8") as file:
        for key, value in system_info.items():
            file.write(f"{key}: {value}\n")

    print(f"[SIM] Recon data saved to {output_file}")


print("=" * 60)
print("        DAY 8 - USB DROP AWARENESS LAB")
print("=" * 60)

print("\n[SIMULATION] Benign USB payload")
print("[SIMULATION] No automatic execution configured.")
print("[SIMULATION] Collecting only local lab system information.\n")

usb_payload_sim()

print("\n" + "=" * 60)
print("             SIMULATION COMPLETE")
print("=" * 60)