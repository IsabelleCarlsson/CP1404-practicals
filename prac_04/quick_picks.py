import random

quick_picks = int(input("How many quick picks? "))

for i in range(0, quick_picks):
    line_of_numbers = []
    for i in range(0, 6):
        line_of_numbers.append(random.randrange(1,45))

    line_of_numbers.sort()
    print("{} {} {} {} {} {}".format(line_of_numbers[0],line_of_numbers[1],line_of_numbers[2],line_of_numbers[3],line_of_numbers[4],line_of_numbers[5]))