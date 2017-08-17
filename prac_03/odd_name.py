def get_name():
    name = input("Name: ")
    while len(name) < 1:
        name = input("Name: ")
    return name


def print_name(name, frequency):
    print(name[::frequency])


def main():
    name = get_name()
    frequency = int(input("Frequency: "))
    print_name(name, frequency)

main()