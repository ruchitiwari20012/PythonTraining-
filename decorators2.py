#Now lets see function within function

def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum
a = funcret(1)
print(a)
