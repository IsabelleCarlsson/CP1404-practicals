total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(0, number_of_items):
    item = float(input("Price of item: "))
    total += item

if total > 100:
    print("Total price for {} items is ${:.2f}".format(number_of_items, total * 0.9))
else:
    print("Total price for {} items is ${:.2f}".format(number_of_items, total))