from types import prepare_class


def factorial(n):
    
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

    prepare_class

number=int(input("Enter the number"))
print(factorial(number))