import sys
import random


from pyfiglet import Figlet

figlet = Figlet()


if len(sys.argv) == 1:
    isRandom = True
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    isRandom = False
else:
    print("Invalid usage")
    sys.exit(1)


figlet.getFonts()

if isRandom == False:
    try:
        font = figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())


msg = input("Input: ")


output = figlet.renderText(msg)

print("Output: ")
print(output)
