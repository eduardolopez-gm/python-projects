import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&()*")


def generate_password():
    password_length = int(input('Enter password length: '))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Do you want to generate a password? Yes / No  ")

if option == "Y" or option == "y":
    generate_password()
elif option == "No" or option == "n":
    print("Program finished")
    quit()
else:
    print('Invalid input')
    quit()
