import requests
from sys import argv, exit

if len(argv) != 2:
    exit('Missing argument')
else:
    try:
        n = float(argv[1])
    except:
        exit('Value error')

try:
    value = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    exit()

val = value.json()
val = float(val['bpi']['USD']['rate'].replace(',',''))

total = n * val
print(f'${total:,.4f}')
