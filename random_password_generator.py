import random

input_value = int(input("Enter password size: "))


def password_generator(given_value):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counting_numbers = "0123456789"
    special_charactors = "@#$%&"

    password = " "
    lengthh_password = [random.choice(lower_alphabet), random.choice(upper_alphabat), random.choice(counting_numbers),
                        random.choice(special_charactors)]

    for i in range(given_value):
        password = password + random.choice(lengthh_password)

    return password


print("Your random password is: ", password_generator(input_value))
