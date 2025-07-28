import subprocess
import re

def check_sleep_settings():
    try:
        # Get active power scheme GUID
        scheme_output = subprocess.check_output("powercfg /getactivescheme", shell=True).decode()
        match = re.search(r"GUID: ([a-fA-F0-9\-]+)", scheme_output)
        if not match:
            return {
                "inactivity_sleep_enabled": None,
                "details": "Could not retrieve active power scheme"
            }

        guid = match.group(1)

        # Check standby timeout for AC (plugged-in) mode
        timeout_output = subprocess.check_output(
            f"powercfg /query {guid} SUB_SLEEP STANDBYIDLE", shell=True
        ).decode()

        timeout_match = re.search(r"Power Setting Index: (\d+)", timeout_output)
        if not timeout_match:
            return {
                "inactivity_sleep_enabled": None,
                "details": "Could not find sleep timeout index"
            }

        timeout_seconds = int(timeout_match.group(1))
        timeout_minutes = timeout_seconds // 60

        return {
            "inactivity_sleep_enabled": timeout_minutes <= 10,
            "details": f"Sleep timeout set to {timeout_minutes} minutes"
        }

    except Exception as e:
        return {
            "inactivity_sleep_enabled": None,
            "details": f"Error: {str(e)}"
        }
