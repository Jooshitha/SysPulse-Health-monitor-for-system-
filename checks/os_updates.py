import platform

def check_os_up_to_date():
    try:
        # Get full version string, e.g., '10.0.26100'
        full_version = platform.version()

        # Extract just the build number (e.g., 26100 from '10.0.26100')
        build_str = full_version.split(".")[-1]
        current_build = int(build_str)

        # Define latest known Windows 11 build (you can adjust as needed)
        latest_known_build = 26100

        if current_build >= latest_known_build:
            return {"os_up_to_date": True, "details": f"Build {current_build} is up to date."}
        else:
            return {"os_up_to_date": False, "details": f"Build {current_build} is outdated. Latest is {latest_known_build}."}
    except Exception as e:
        return {"os_up_to_date": None, "details": f"Error: {str(e)}"}
