def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    n = ip.split('.')
    if len(n) != 4:
        return False
    for _ in n:
        if not _.isdigit():
            return False
        elif not 0 <= int(_) < 256:
            return False
    return True


if __name__ == "__main__":
    main()
