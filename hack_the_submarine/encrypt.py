def main():
    text = input()
    result = ""
    for char in text:
        if char.isalpha() and char.islower():
            if ord(char)+3 >122:
                char = chr(ord(char)-23) #97+3
            else:
                char = chr(ord(char)+3)
        elif char.isalpha() and char.isupper():
            if ord(char)+3 >90:
                char = chr(ord(char)-23) #65+3
            else:
                char = chr(ord(char)+3)
        else:
            char = char
        result += char
    print(result)
main()
