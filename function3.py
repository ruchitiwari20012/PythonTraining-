def function1(a,b):
    print("Hello you are in function1",a+b)
def function2(a,b):
    average= (a+b)/2
    print(average)
v=function2(5,7)
print(v)

#return none lets use it with return keyword

def function2(a,b):
    average=(a+b)/2
   #print(average)
    return average
v=function2(5,7)
print(v)