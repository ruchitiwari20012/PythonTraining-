Name = "Ruchi"
Description=''' Ruchi is a very nice girl'''

print(Name)
print(Description)

print(Name[0])
print(Name[0:4]) # 0 to n-1
print(Name[:4])
print(Name[0:5])

# String methods
fresh= " Programming with Ruchi"
print(" String Method: ")
print("The length of this string is ", len(fresh))

print(fresh.strip())
print(fresh.lower())
print(fresh.upper())
print(fresh.replace('Ru','Mh'))

nums="1,2,3,4,5,6,7,8,9"
print(nums.split(" , "))