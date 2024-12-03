def converter_to_snake(camel):
    for char in camel:
        if char.isupper():
            print( '_' + char.lower(), end = '')
        else:
            print(char, end = '')
def main():
    camel = input('Enter a varible name in camel: ')
    snake = converter_to_snake(camel)
    print(snake, end = '')

if __name__ == "__main__":
    main()
