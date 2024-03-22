def add(a: int):
    summation = 0
    while a >= 0:
        summation += a
        a -= 1
    return summation


number = int(input("Please write an integer"))

summation = add(number)
print("Sum of the number from " + str(number) + " to 1 is: " + str(summation))
