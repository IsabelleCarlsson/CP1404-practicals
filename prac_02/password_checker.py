"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: {}".format(SPECIAL_CHARACTERS))
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {} character password is valid: {}".format(str(len(password)), password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        return False
    else:
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 1
        for char in password:
            if char.isdigit():
                count_digit += 1
            elif char.isupper():
                count_upper += 1
            elif char.islower():
                count_lower += 1
            elif SPECIAL_CHARS_REQUIRED:
                count_special = 0
                if char in SPECIAL_CHARACTERS:
                    count_special += 1

        if 0 in {count_lower, count_upper, count_digit, count_special}:
            return False

        return True

main()