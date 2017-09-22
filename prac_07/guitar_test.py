""" CP1407 Practical 7 - Guitar Class Testing """

from guitar import Guitar

guitars = []

# Input lines for testing purposes
#guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
#guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

guitar_name = input("Name: ")
while not guitar_name == "":
    guitar_name = input("Name: ")
    if guitar_name == "":
        break
    else:
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print("{} ({}) : ${:,.2f} added.".format(guitar_name, guitar_year, guitar_cost))


for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))