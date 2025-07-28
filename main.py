from checks import disk_encryption, os_updates, antivirus, sleep_settings

if __name__ == "__main__":
    disk_result = disk_encryption.check_disk_encryption()
    print("[Disk Encryption Status]")
    print(disk_result)

    os_result = os_updates.check_os_up_to_date()
    print("\n[OS Update Status]")
    print(os_result)

    antivirus_result = antivirus.check_antivirus_status()
    print("\n[Antivirus Status]")
    print(antivirus_result)

    sleep_result = sleep_settings.check_sleep_settings()
    print("\n[Sleep Settings]")
    print(sleep_result)