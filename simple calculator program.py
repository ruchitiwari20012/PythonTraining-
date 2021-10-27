# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def sub(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def mul(num1,num2):
    return num1 * num2

# Function to divide two numbers
def div(num1,num2 ):
    return num1 / num2

print("Please select operation -\n" \
    "1. Add\n" \
    "2.Subtract\n" \
    "3.Multiply\n" \
    "4.Divide\n")
#Take input from the user
select = int(input("Select operation from 1,2,3,4:"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter the second number "))

if select == 1:
    print(number_1, "+", number_2, '=',
                    add(number_1,number_2))

elif select == 2:
    print(number_1, "-", number_2, '=',
                    sub(number_1,number_2))

elif select == 3:
    print(number_1, "*", number_2, '=',
                    mul(number_1,number_2))

elif select == 4:
    print(number_1, "/", number_2, '=',
                    div(number_1,number_2))

else:
    print("Invalid Input")

