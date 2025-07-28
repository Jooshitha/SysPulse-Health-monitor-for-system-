import time
import hashlib
import json
import datetime
from checks import disk_encryption, os_updates, antivirus, sleep_settings
from utils.reporter import get_machine_id

CHECK_INTERVAL_SECONDS = 1800  # 30 minutes

def get_system_status():
    return {
        "machine_id": get_machine_id(),
        "disk_encryption": disk_encryption.check_disk_encryption(),
        "os_updates": os_updates.check_os_up_to_date(),
        "antivirus": antivirus.check_antivirus_status(),
        "sleep_settings": sleep_settings.check_sleep_settings()
    }

def hash_status(status):
    status_json = json.dumps(status, sort_keys=True)
    return hashlib.sha256(status_json.encode()).hexdigest()

def run_daemon():
    print("[Daemon] Starting system monitor daemon...")
    last_hash = None

    while True:
        status = get_system_status()
        current_hash = hash_status(status)

        if current_hash != last_hash:
            print("[Daemon] System state changed.")
            print(json.dumps(status, indent=4))

            with open("system_log.jsonl", "a") as log_file:
                log_file.write(json.dumps({
                    "timestamp": datetime.datetime.now().isoformat(),
                    "status": status
                }) + "\n")

            last_hash = current_hash
        else:
            print("[Daemon] No change detected.")

        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    run_daemon()
