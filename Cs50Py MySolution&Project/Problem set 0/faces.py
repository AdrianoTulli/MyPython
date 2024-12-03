def convert(user_input):
    if user_input == ":)":
        return "🙂"
    else:
        return "🙁"

def main():
    user_input = input("Enter text: ")
    text = user_input.split()
    for word in text:
        if word == ":)" or word == ":(":
            i = text.index(word)
            text[i] = print(convert(word), end=" ")
        else:
             print(word, end=" ")
    print("")

if __name__ == "__main__":
    main()
