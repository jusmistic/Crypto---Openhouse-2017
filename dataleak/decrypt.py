def main():
    text = input()
    text = text[::-1]
    result = ""
    for char in text:
        char = chr(ord(char)-3)		
        result += char
    print(result)
main()
        
