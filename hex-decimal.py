hexNumbers = { 
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 
}

def hexToDec(hexNum):
    """
    Converts a string hexadecimal number into an integer decimal.
    If hexNum is not a valid hexadecimal number, returns None.
    """
    try:
        # Python's built-in int() can convert a hex string to an integer
        # The second argument '16' specifies the base (hexadecimal)
        decimal_value = int(hexNum, 16) 
        return decimal_value
    except ValueError:
        # This handles cases where the input string is not a valid hex number
        return None

# Example Usage:
print(f"'A' converts to: {hexToDec('A')}")
print(f"'1F' converts to: {hexToDec('1F')}")
print(f"'Z' converts to: {hexToDec('Z')}") # Invalid input returns None
