def main():
    user_input = input('Greeting: ').strip().lower()
    x = value(user_input)
    print(f'${x}')

def value(user_input):

    if user_input.startswith('hello'):
        val = 0
    elif user_input.startswith('h'):
        val = 20
    else:
        val = 100
    return val

if __name__ == '__main__':
    main()
