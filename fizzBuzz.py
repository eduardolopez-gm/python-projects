print("\n================================")
print("Welcome to FizzBuzz challenge")
print("================================")
number = int(input("Enter a number to calculate the FizzBuzz challenge: "))

for actual_value in range(1, number+1):
    # print(actual_value)
    if ((actual_value % 3 == 0) & (actual_value % 5 == 0)): 
        print("FizzBuzz")
    elif (actual_value % 3 == 0):
        print("Fizz")
    elif (actual_value % 5 == 0):
        print("Buzz")
    else:
        print(actual_value)
print("\n================================")
print("Challenge finished")
print("================================")
