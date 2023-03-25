"""
function main()
    get password
    print  '*' * len


function get_valid_password()
    get password
    while len(password) < Minimum length:
        get password
    return password
"""

PASSWORD_LENGTH = 10


def main():
    password = get_valid_password("Please entry your password(at least 10 characters): ")
    print("Your password: ", "*" * len(password))


def run_test():
    password = get_valid_password("Please entry your password(at least 10 characters): ")
    print(password)


def get_valid_password(prompt):
    entry_password = input(prompt)
    while len(entry_password) < PASSWORD_LENGTH:
        print("Less than 10 characters, please re-enter!")
        entry_password = input(prompt)

    return entry_password


main()

