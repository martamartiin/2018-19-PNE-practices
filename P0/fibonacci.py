n = 10
def fibonacci(n) :
    l_fibonacci= [0, 1]
    for e in range(n-2) :
        i = l_fibonacci[e] + l_fibonacci[e+1]
        l_fibonacci.append(i)
    return l_fibonacci

print("The n first numbers of the fibonacci series are:",fibonacci(n))

