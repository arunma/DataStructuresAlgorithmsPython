def convert(char, start, rotational_factor, modu):
    order = ord(char) #eg. Z=90
    currCharOrder = (order - start + rotational_factor) % modu #2
    currCharAct = currCharOrder + start #C=67
    return chr(currCharAct)


def rotationalCipher(input, rotation_factor):
    uppA = ord("A")
    lowerA = ord('a')
    num0=ord('0')

    result = ""
    for c in input:
        if c.isalpha() and c.isupper():
            result += convert(c, uppA, rotation_factor, 26)
        elif c.isalpha() and c.islower():
            result += convert(c, lowerA, rotation_factor, 26)
        elif c.isnumeric():
            result += convert(c, num0, rotation_factor, 10)
        else:
            result += c
    return result


if __name__ == '__main__':
    print(rotationalCipher("Zebra-493?", 3))
