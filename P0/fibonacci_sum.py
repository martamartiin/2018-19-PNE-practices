import math
n = int(input("Introduce here the number:"))
def fibonacci(n) :
    l_fibonacci= [0, 1]
    for e in range(n-2) :
        i = l_fibonacci[e] + l_fibonacci[e+1]
        l_fibonacci.append(i)
    return l_fibonacci
def fibonacci_sum(n):
    l_numbers = fibonacci(n)
    summed = sum(l_numbers)
    return summed
print("The result of adding the first n numbers of the fibonacci series is:", fibonacci_sum(n) )

