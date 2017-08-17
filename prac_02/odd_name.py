name = input("Name: ")

while len(name) < 1:
    name = input("Name: ")

print(name[::2])