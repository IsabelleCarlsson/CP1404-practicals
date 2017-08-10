LOWER = 33
UPPER = 127

character = input("Enter a character: ")
print("The ASCII code for {} is {}".format(character, ord(character)))
number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))

while number > UPPER or number < LOWER:
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
print("The character for {} is {}".format(number, chr(number)))

for i in range(33,128):
    print("{:>3}{:>4}".format(i, chr(i)))