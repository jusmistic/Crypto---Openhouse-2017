def main():
    text = input()
    result = ""
    for char in text:
        if char.isalpha() and  char.islower():
            if ord(char)- 3 < 97:
                re_val = 97-(ord(char)-3)
                char = chr(122-re_val+1)
            else:
                char = chr(ord(char)-3)
        elif char.isalpha() and char.isupper():
            if ord(char)- 3 < 65:
                re_val = 65-(ord(char)-3)
                char = chr(90-re_val+1)
            else:
                char = chr(ord(char)-3)
        else:
            char = char
        result += char
    print(result)
main()
