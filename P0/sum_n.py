import math
numb= input("Introduce here the number you want to add:")
def sum_N(numb):
    if numb.isalpha() == True:
        print("Sorry, it must be an integer, try it again.")
        numb = input("Introduce here the number you want to add:")

    numbers = range(1, int(numb)+1)
    summed = sum(numbers)
    return summed
print(sum_N(numb))