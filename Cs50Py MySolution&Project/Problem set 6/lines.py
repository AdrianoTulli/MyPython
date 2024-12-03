import sys


def control():
    if len(sys.argv) > 2:
        sys.exit('Too much argument')
    elif len(sys.argv) < 2:
        sys.exit('Need more argument')
    elif not sys.argv[1].rsplit('.')[1] == 'py':
        sys.exit('Not a Python file')
    return


def main():
    control()
    try:
        with open(sys.argv[1], 'r') as file:
            num_line = 0
            for _ in file:
                if not _.lstrip().startswith('#') and not _.lstrip() == '':
                        num_line += 1
            print(num_line)
    except:
        raise FileNotFoundError


if __name__ == '__main__':
    main()
