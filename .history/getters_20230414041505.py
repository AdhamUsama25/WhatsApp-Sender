import functions


def get_names(n):
    names = []
    print("Enter the receivers names: ")

    for i in range(n):
        names.append(input())

    return names


def get_numbers(n):
    numbers = []

    calling_code_flag = input(
        """
    Does your numbers have the calling codes?
    Enter y if yes
    Enter n if no
        """)

    if calling_code_flag == 'n':
        print(
            "Enter the receivers phone numbers without the calling code. Example: 01...: ")

        for i in range(n):
            number = functions.add_zero(input())
            numbers.append(f"+2{number}")

    elif calling_code_flag == 'y':
        print("Enter the receivers phone numbers with the calling code. Example: +201...: ")

        for i in range(n):
            number = functions.add_zero(input())
            numbers.append(f"{number}")
    else:
        print("Please, enter a valid input")
        get_numbers(n)

    return numbers


def get_message():
    print("Enter the message and replace the name of the receiver with <name>.")

    msg = ""

    while True:
        line = input()
        if line != 'end msg':
            msg += f"{line}\n"
        else:
            break

    functions.display_msg(msg)

    continue_flag = input('''
Do you wish to continue the message?
Enter y if yes and n if no
    ''')

    if continue_flag == 'y':
        get_message()
    elif continue_flag == 'n':
        return msg
    else:
        print("Wrong input.")
        get_message()
