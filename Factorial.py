def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)

print('Factorial of 5: ', factorial(5))
