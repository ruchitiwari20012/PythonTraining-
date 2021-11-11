l=10 # global 
def function1 (n):
    #l=5 # local
    m=8 # local
    global l
    l = l + 45 
    print(l,m)
    print(n, "I have printed")
function1("This is me")
#print(l)