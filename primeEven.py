def check_prime_even(number):
    
    result = f"{number} "
    #Prime
    if number > 1:
        for index in range(2, number):
            if number % index == 0:
                result += "no es primo "
                break
        else:
            result += "es primo, "
    else:
        result += "no es primo "

    #Even
    result += "y es par" if number % 2 == 0 else "y es impar"

    print(result)

check_prime_even(1)
check_prime_even(3)
check_prime_even(4)
check_prime_even(5)
check_prime_even(2)
