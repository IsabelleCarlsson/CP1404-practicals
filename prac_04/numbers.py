def main():
    numbers = []
    count = 1
    number = int(input("Number 1: "))
    numbers.append(number)
    while number > 0:
        number = int(input("Number {}: ".format(count + 1)))
        numbers.append(number)
        count += 1

    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[len(numbers)-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))
main()