def main():
    user_input = input('Sentence to short: ')
    user_input = shorten(user_input)
    print(user_input)


def shorten(user_input):
    #vocals = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vocals = ['a', 'e', 'i', 'o', 'u']
    for letter in user_input:
        if letter in vocals:
            user_input = user_input.replace(letter, '')
    return user_input

if __name__ == '__main__':
    main()
