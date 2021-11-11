x=89
def harry():
    x=20
    def rohan():
        global x

    rohan()
    print("before calling rohan ()",x)

harry()
print(x)