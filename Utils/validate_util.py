def validate_values(values: dict, exceptions: list =[]) -> bool:
    """
    Checks that no 'string' values are empty.
    values: dictionary data
    exceptions: list of 'keys' allowed to be empty (basically don't check them)
    """

    for key, val in values.items():
        if key == "country" and val == "Select Country":
            return False
        if key in exceptions:
            continue
        if isinstance(val, str) and not val.strip():
            return False
        
    return True

