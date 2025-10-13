def fibonacci(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    #for i in range(1, n+1):
        #result += fibonacci(i)

    return fibonacci(n-1) + fibonacci(n-2)

while True:

    user_input = input("Enter a positive integer below 46: ")

    if user_input.isdigit() and int(user_input) <= 45:
        number = int(user_input)
        print(fibonacci(number))
        break
    else:
        print("Invalid input, try again")

