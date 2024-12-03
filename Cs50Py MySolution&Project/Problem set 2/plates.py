def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) <= 6 and len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        for char in s:
            if char.isdigit():
                f_num = s.index(char)
                if int(char) != 0:
                    if s[f_num:].isdigit():
                        return True
                else:
                    return False
        return True


main()
