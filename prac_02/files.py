# Task 1
text_file = open('name.txt', 'w')
name = input("What is your name?\n")
print(name, file=text_file)
text_file.close()

# Task 2
text_file = open("name.txt", "r")
print("Your name is", text_file.read())
text_file.close()

# Task 3/4
text_file = open("numbers.txt", "r")
total = 0
for line in text_file:
    total += int(line)
print(total)
text_file.close()