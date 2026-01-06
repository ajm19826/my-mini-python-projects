import json

# Your provided encodeString logic
def encodeString(stringVal):
    if not stringVal: return []
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

# Your provided decodeString logic
def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        # JSON may load tuples as lists; item[0] is the char, item[1] is the count
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

def encodeFile(filename, newFilename):
    """Reads a text file, encodes it using RLE, and saves it as a JSON file."""
    with open(filename, 'r') as file:
        # Use .read() to capture everything including newlines
        content = file.read()
    
    encoded_content = encodeString(content)
    
    with open(newFilename, 'w') as file:
        # JSON is used to save the list of tuples/lists accurately
        json.dump(encoded_content, file)

def decodeFile(filename):
    """Loads a JSON file, decodes the RLE data, and returns the original string."""
    with open(filename, 'r') as file:
        encoded_content = json.load(file)
    
    # decodeString reconstructs the original string (including \n characters)
    return decodeString(encoded_content)

# Usage Example:
# encodeFile('10_04_challenge_art.txt', 'encoded_art.json')
# print(decodeFile('encoded_art.json'))
