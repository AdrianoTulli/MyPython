def main():
    user_question = input("What is the answer for the great question of life? ").strip()

    if user_question == '42' or user_question.lower() == 'forty two' or user_question.lower() == 'forty-two':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
