user_name = str(input("Enter name: "))
print("(H)ello\n(G)oodbye\n(Q)uit\n")
user_choice = str(input(">>> "))

while user_choice.upper() != "Q":
    if user_choice.upper() == "H":
        print("Hello " + user_name)
    elif user_choice.upper() == "G":
        print("Goodbye " + user_name)
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit\n")
    user_choice = str(input(">>> "))
print("Finished.")