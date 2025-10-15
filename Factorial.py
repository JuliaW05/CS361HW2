def factorial(n):

    #if type(n) is not int:
        #return "Factorial is only available for integers"

    if n == 0:
        return 1

    #if n < 0:
        #return "Factorial is not available for negative numbers"

    #result = 1
    #for i in range (1, n + 1):
        #result *= i

    return n*factorial(n-1)

while True:

    user_input = input("Enter a positive integer: ")

    if user_input.isdigit():
        number = int(user_input)
        print(factorial(number))
        break
    else:
        print("Invalid input, try again")


#print(factorial(number))
#print(factorial(5))
#print(factorial(-1))
#print(factorial(-50))
#print(factorial(10))
#print(factorial(120))
#print(factorial(1.5))
#print(factorial(1.3))
