m = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").title()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
                break
        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            if month in m and int(day) >= 1 and int(day) <= 31:
                month = m.index(month) +1
                break
    except:
        print()
        pass
print(f"{int(year)}-{int(month):02}-{int(day):02}")
