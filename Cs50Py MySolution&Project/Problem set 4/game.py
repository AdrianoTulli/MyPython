import random

while True:
    try:
        lv = input('Level: ')
        if lv.isnumeric():
            lv = int(lv)
        else:
            raise Exception
        if lv > 0:
            break
        else:
            raise Exception
    except:
        pass

x = random.randint(1, lv)
n = 0

while n != x:
    n = input('Guess: ')
    if n.isnumeric() > 0:
        n = int(n)
    else:
        continue
    if n < x:
        print('Too small!')
    elif n > x:
        print('Too large!')
    else:
        print('Just right!')
        break
