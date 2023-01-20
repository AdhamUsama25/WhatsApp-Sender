def display_msg(msg):
    if '<name>' in msg:
        print('If the receiver name is Ahmed, the message will be:')
        print(msg.replace('<name>', 'Ahmed'))
    else:
        print('Your msg is: ')
        print(msg)


def add_zero(number):
    if number[0] != 0:
        number = f"0{number}"

    return number
