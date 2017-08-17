def main():
    text = input()
    result = []
    print(" ".join(format(ord(char), 'b') for char in text))
main()
