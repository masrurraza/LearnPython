def factorial(number):
    result = 1
    for num in range(number, 0, -1):
        result *= num
    return result


def factorialw(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorialw(3))
print(factorialw(4))
print(factorialw(5))

for number in range(5, 1, -1):
    print(number)
