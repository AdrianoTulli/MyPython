import sys
import csv

def control():
    if len(sys.argv) > 3:
        sys.exit('Too much argument')
    elif len(sys.argv) < 3:
        sys.exit('Need more argument')
    if not sys.argv[1].endswith('.csv') or not sys.argv[2].endswith('.csv'):
        sys.exit('Not a CSV file')

def rewrite():
    students = []
    with open(sys.argv[1], 'r') as rfile:
        reader = csv.DictReader(rfile)
        for row in reader:
            last, first = row['name'].split(',')
            students.append({
                'first': first.strip(),
                'last': last.strip(),
                'house': row['house']
            })

    with open(sys.argv[2], 'w', newline='') as wfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(wfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)


def main():
    control()
    rewrite()

if __name__ == '__main__':
    main()
