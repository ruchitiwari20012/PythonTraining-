def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return  n * factorial_recursive(n-1)
number=int(input("Enter the number "))
print("Factorial using iterative method",factorial_recursive(number))