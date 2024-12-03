import re

def main():
    user_input = input('Text: ')
    print(count(user_input))

def count(s):
    return len(re.findall(r'\bum\b', s.lower()))

if __name__ == '__main__':
    main()
