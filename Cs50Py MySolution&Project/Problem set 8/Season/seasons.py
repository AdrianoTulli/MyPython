import datetime
import inflect
import re
import sys

def converter(time_delta):
    x = inflect.engine()
    _ = (f'{x.number_to_words(time_delta, andword= '').replace(' and', ',')}' + ' minutes')
    print(_.capitalize())

def time_to_minute(user_input):
    time_delta = datetime.date.today() - datetime.date.fromisoformat(user_input)
    converter(int(time_delta.total_seconds() / 60))

def def_user_input():
    print('YYYY-MM-DD')
    user_input = input('Birth Date: ')
    if re.match(r'^\d\d\d\d-\d\d-\d\d$', user_input):
        return user_input
    else:
        print('Invalid input')
        sys.exit(1)

def main():
    user_input = def_user_input()
    time_to_minute(user_input)

if __name__=='__main__':
    main()

