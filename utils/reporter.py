import uuid

def get_machine_id():
    """
    Returns a unique machine identifier using the MAC address.
    """
    return str(uuid.getnode())
