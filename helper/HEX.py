import re
hexString=r'^#[a-fA-F\d]{3}$|^#[a-fA-F\d]{6}$|^#[a-fA-F\d]{8}$'
def ishex(hex):
    """Checks the length of the hex string if the string is 3, 6, 8  character hex"""
    return bool(re.compile(hexString).search(hex))
def hexlen(hex):
    """Checks if given string is pure hex string or not"""
    return len(hex.replace('#','')) if ishex(hex) else False