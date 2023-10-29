import inflect

p = inflect.engine()

names_list = []

while True:
    try:
        name = input("Name: ")
        names_list.append(name)
    except EOFError:
        print()
        break

output = p.join(names_list)
print("Adieu, adieu, to " + output)
