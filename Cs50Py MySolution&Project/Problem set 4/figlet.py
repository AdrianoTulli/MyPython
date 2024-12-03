from pyfiglet import Figlet
import sys
import random

font_list = Figlet().getFonts()

if len(sys.argv) == 1:
    font_list = random.choice(font_list)
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in font_list:
        font_list = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")


user_input = input("Input: ")
print(Figlet(font=font_list).renderText(user_input))
