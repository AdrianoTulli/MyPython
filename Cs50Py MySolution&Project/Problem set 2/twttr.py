vocals = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
user_input = input("Sentence to shorten: ")

for letter in user_input:
    if letter in vocals:
        continue
    print(letter, end='')
print('')
