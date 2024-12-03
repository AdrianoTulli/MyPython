import sys
import tabulate
import csv

if len(sys.argv) > 2:
    sys.exit('Too much argument')
elif len(sys.argv) < 2:
    sys.exit('Need more argument')
elif not sys.argv[1].endswith('.csv'):
         sys.exit('Not a CSV file')


try:
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        print(tabulate.tabulate(reader, headers='keys', tablefmt='grid'))
except:
    raise FileNotFoundError
