def main():
    x = level()
    print(x)

def level():
    while True:
        try:
            fract = input("Fraction: ").strip().split("/")
            lv = round(float((int(fract[0]) / int(fract[1]))*100))
            if int(fract[0]) <= int(fract[1]):
                if lv >= 99:
                    print("F")
                elif lv <= 1:
                    print("E")
                else:
                    print(f"{lv}%")
                exit()
            else:
                return level()
        except (ValueError, ZeroDivisionError):
            print("Denominator can't be 0, Format should be: x/y")
            continue
main()
