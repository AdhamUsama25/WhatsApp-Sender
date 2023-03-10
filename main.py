import opening
import getters
import send

# Opening

opening.opening()

# Getting Data


number_of_receivers = int(input("Enter the number of receivers: "))

myMsg = getters.get_message()

phone_numbers_list = getters.get_numbers(number_of_receivers)

if '<name>' in myMsg:
    names_list = getters.get_names(number_of_receivers)
else:
    names_list = []

# Sending Messages:

send.sender(number_of_receivers, myMsg, names_list, phone_numbers_list)
