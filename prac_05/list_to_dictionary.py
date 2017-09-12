names = []
dobs = []

for person in range(0,5):
    user_name = input("Please enter your name: ")
    names.append(user_name)
    user_dob = input("Enter you date of birth (eg. 16/07/1997): ").split("/")
    dobs.append(user_dob)

print(dict(zip(names, dobs)))
