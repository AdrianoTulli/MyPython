import sys
from PIL import Image, ImageOps


def check_argv():
    if len(sys.argv) > 3:
        sys.exit('Too many argument')
    elif len(sys.argv) < 3:
        sys.exit('Need more argument')
    if not sys.argv[1].endswith('.jpg'):
        sys.exit('Not a .jpg file')
    if sys.argv[1].endswith('.jpg') != sys.argv[2].endswith('.jpg'):
        sys.exit('Input and output hav different extension')
    return sys.argv[1], sys.argv[2]


def main():
    sys.argv[1], sys.argv[2] = check_argv()
    try:
        shirt = Image.open('shirt.png')
    except FileNotFoundError:
        exit('shirt.png file not found in the same directory')
    try:
        muppet = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f'{sys.argv[1]} file not found')

    muppet = ImageOps.fit(muppet, shirt.size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])


if __name__ == '__main__':
    main()
