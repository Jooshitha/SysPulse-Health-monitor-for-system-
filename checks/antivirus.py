import subprocess
import json
import datetime
import re

def convert_dotnet_date(dotnet_date_str):
    match = re.search(r"/Date\((\d+)\)/", dotnet_date_str)
    if match:
        timestamp = int(match.group(1)) / 1000
        return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    return "Unknown"

def check_antivirus_status():
    try:
        command = [
            "powershell",
            "-Command",
            "Get-MpComputerStatus | Select-Object -Property AMServiceEnabled, AMRunningMode, AntivirusEnabled, AntivirusSignatureLastUpdated | ConvertTo-Json"
        ]

        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout.strip()

        if not output:
            raise Exception("No output from PowerShell command.")

        data = json.loads(output)

        last_updated = convert_dotnet_date(data.get("AntivirusSignatureLastUpdated", ""))

        if data.get("AntivirusEnabled"):
            return {
                "antivirus_enabled": True,
                "details": f"Running Mode: {data.get('AMRunningMode', 'Unknown')}, Signature Last Updated: {last_updated}"
            }
        else:
            return {"antivirus_enabled": False, "details": "Antivirus is disabled"}

    except Exception as e:
        return {"antivirus_enabled": None, "details": f"Error: {str(e)}"}
