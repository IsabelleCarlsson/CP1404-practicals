'''
Write a program that asks the user for an indefinite set of strings - until an empty string is entered - then
prints all of the strings that were repeated.
E.g. if the user entered: “hello”, “world is good”, “hello”, “john”, “good”… the program would print
“Strings repeated: hello”.
If no repeated strings are entered, the program should print “No repeated strings entered”.
'''

string_input = input("String: ")
strings = []

while string_input:
    string_input = input("String: ")
    strings.append(string_input)


for line in strings:
    count = 0
    print(line)
    for j in strings:
        print(j)
        if line == j:
            count += 1
            print(count)
        elif count > 1:
            print("Strings repeated: {}".format(j))
