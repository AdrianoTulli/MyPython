def main():
    user_input = input('Expression: ').split()
    x = float(user_input[0])
    y = float(user_input[2])
    if user_input[1] == '+':
        print(x + y)
    elif user_input[1] == '-':
        print(x - y)
    elif user_input[1] == '*':
        print(x * y)
    elif user_input[1] == '/':
        print(x / y)
    else:
        print('Error: Unexpected Operator')

if __name__ == main():
    main()
