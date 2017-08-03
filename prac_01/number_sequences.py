first_number = int(input("Please enter the first number: "))
second_number = int(input("PLease enter the second number: "))

print("1. Show the even numbers from {} to {}".format(first_number, second_number))
print("2. Show the odd numbers from {} to {}".format(first_number, second_number))
print("3. Show the squares numbers from {} to {}".format(first_number, second_number))
print("4. Exit the program")

menu_choice = str(input(">>> "))

while menu_choice != "4":
    if menu_choice == "1":
        for i in range(first_number, second_number):
            if i % 2 == 0:
                print(i)
            else:
                none
    elif menu_choice == "2"
        for i in range(first_number, second_number):
            if i % 2 == 1:
                print(i)
            else:
                none
    elif menu_choice == "3"
        for i in range(first_number, second_number):
            if i ** (0.5) %
