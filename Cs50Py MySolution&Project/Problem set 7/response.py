import validators

if validators.email(input('Enter your Email: ')):
    print('Valid')
else:
    print('Invalid')
