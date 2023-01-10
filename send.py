import pywhatkit


def send_without_photo(n, message, names, numbers):
    for i in range(n):
        msg = message.replace('<name>', names[i])

        print(f'Sending message #{i + 1}')

        pywhatkit.sendwhatmsg_instantly(numbers[i], msg, 10, True)

        print(f'Message #{i + 1} sent.')

        print(f'{n - i - 1} messages remaining...')
        print('=============================================')


def send_with_photo(n, message, names, numbers):

    photo = input('Enter the photo path: ')

    for i in range(n):
        msg = message.replace('<name>', names[i])

        print(f'Sending message #{i + 1}')

        pywhatkit.sendwhats_image(numbers[i], photo, msg, 25, True)

        print(f'Message #{i + 1} sent.')

        print(f'{n - i - 1} messages remaining...')
        print('=============================================')


def sender(n, message, names, numbers):
    print('1. Send a text message')
    print('2. Send a photo message')
    flag = input()

    if flag == '1':
        send_without_photo(n, message, names, numbers)
    elif flag == '2':
        send_with_photo(n, message, names, numbers)
    else:
        print('Enter a valid value')
        sender()
