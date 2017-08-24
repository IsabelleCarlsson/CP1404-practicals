LOWER = 33
UPPER = 127

"""character = input("Enter a character: ")
print("The ASCII code for {} is {}".format(character, ord(character)))

for i in range(33,128):
    print("{:>3}{:>4}".format(i, chr(i)))"""

def get_number(lower,upper):
    invalid_number = True
    while invalid_number:
        try:
            number = int(input("Enter a number between {}-{}:\n>>> ".format(lower, upper)))
            invalid_number = False
        except ValueError:
            print("Please enter a valid number!")

    while number > UPPER or number < LOWER:
        print("Please enter a valid number!")
        number = int(input("Enter a number between {}-{}:\n>>> ".format(lower, upper)))

    return number

def main():
    number = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(number, chr(number)))

main()