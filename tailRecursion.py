def fib(n):
    x = 0
    y = 1

    while n > 0:
        xTemp = x
        x = y
        y = xTemp + y
        n = n - 1

    return x

while True:

    user_input = input("Enter a positive integer below 46: ")

    if user_input.isdigit() and int(user_input) <= 45:
        number = int(user_input)
        print(fib(number))
        break
    else:
        print("Invalid input, try again")