import subprocess

def check_disk_encryption():
    try:
        result = subprocess.run(
            ['manage-bde', '-status', 'C:'],
            capture_output=True,
            text=True
        )
        output = result.stdout
        print("=== Raw manage-bde Output ===")
        print(output)

        # Normalize spaces for easier matching
        normalized = output.replace(" ", "").lower()

        if "protectionstatus:protectionon" in normalized:
            return {"disk_encryption": True, "details": "BitLocker is ON"}
        elif "protectionstatus:protectionoff" in normalized:
            return {"disk_encryption": False, "details": "BitLocker is OFF"}
        else:
            return {"disk_encryption": None, "details": "Unable to determine BitLocker status"}
    except Exception as e:
        return {"disk_encryption": None, "details": f"Error: {str(e)}"}
