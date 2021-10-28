# Python program to check if the number is an Armstrong number or not

# Take the input from the user
num = int(input("Enter a number: "))

# initialize the sum
sum = 0
# find sum of the cubes of every digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit **3
    temp//=10


# display the result
if num==sum:
    print(num," is a Amstrong Number")
else:
    print(num,'is not an Amstrong Number')
