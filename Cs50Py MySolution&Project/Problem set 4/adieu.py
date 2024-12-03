name_list = []
while True:
    try:
        name = input('Name: ')
        name_list.append(name)
    except:
        break

print('Adieu, adieu, to',end=' ')
if len(name_list)>2:
    for n in name_list[:-1]:
        print(n, end=', ')

    print('and', name_list[-1])
else:
    print(name_list[0], end=' ')
    if len(name_list)==2:
        print('and', name_list[1])
