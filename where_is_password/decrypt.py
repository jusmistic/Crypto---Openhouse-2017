def main():
    text = input()
    result = ""
    text = text.split()
    for index in text:
        result += chr(int(index, 2))
    print(result)
main()
