def add(number1, number2):
    print(str(number1) + " + " + str(number2) + " = " + str(number1 + number2) + "\n")


def sub(number1, number2):
    print(str(number1) + " - " + str(number2) + " = " + str(number1 - number2) + "\n")


def multiply(number1, number2):
    print(str(number1) + " * " + str(number2) + " = " + str(number1 * number2) + "\n")


def division(number1, number2):
    if number2 == 0:
        print('You cant do this operation')
    else:
        format_number = f"{(number1/number2): .2f}"
        print(str(number1) + " / " + str(number2) + " = " + str(format_number) + "\n")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input('Enter your choice:  ')

    if choice == 'a' or choice == 'A':
        print('Addition selected')
        value1 = int(input('Enter first number '))
        value2 = int(input('Enter second number '))
        add(value1, value2)
    elif choice == 'b' or choice == 'B':
        print('Subtraction selected')
        value1 = int(input('Enter first number '))
        value2 = int(input('Enter second number '))
        sub(value1, value2)
    elif choice == 'c' or choice == 'C':
        print('Multiplication selected')
        value1 = int(input('Enter first number '))
        value2 = int(input('Enter second number '))
        multiply(value1, value2)
    elif choice == 'd' or choice == 'D':
        print('Division selected')
        value1 = int(input('Enter first number '))
        value2 = int(input('Enter second number '))
        division(value1, value2)
    elif choice == 'e' or choice == 'E':
        print('Program finished')
        quit()
