def cipher(text, s):
    # Your code goes here
    result = ""
    for i in range(len(text)):
        char = text[i]

        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result
