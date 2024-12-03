def main():
    user_input = input('Please enter the time: ').strip()
    time = convert(user_input)
    if 7<= time <= 8:
        print('Breakfast time')
    elif 12<= time <= 13:
        print('Lunch time')
    elif 18<= time <= 19:
        print('Dinner time')
    else:
        print('Diet time')

def convert(time):
    if 'p.m.' in time:
        time = time.replace('p.m.', '')
        hours, minutes = map(float, time.split(':'))
        converted_time = 12 + hours + minutes/60
    else:
        if 'a.m.' in time:
            time = time.replace('a.m.', '')
        hours, minutes = map(float, time.split(':'))
        converted_time = hours + minutes/60

    return converted_time

if __name__ == '__main__':
    main()
