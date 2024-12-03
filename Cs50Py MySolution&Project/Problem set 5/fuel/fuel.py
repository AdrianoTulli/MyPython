def main():
    fract = input("Fraction: ").strip().split("/")
    percentage = convert(fract)
    level = gauge(percentage)
    print(f'Actual fuel level is: {level}')


def convert(fract):
    while True:
        try:
            if fract[0] > fract[1]:
                main()
            else:
                return round(float((int(fract[0]) / int(fract[1]))*100))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def gauge(percentage):
    lv = int(percentage)
    if 99 <= lv <= 100:
        return("F")
    elif lv <= 1:
        return("E")
    else:
        return(f"{lv}%")


if __name__ == "__main__":
    main()
