def xyz(x):
    swicher= {
        0:'Zero',
        1:'One',
        2:'Two',
        3:'Three',
            }
    return swicher.get(x,'option not available')
n = int(input("enter choice"))
c = xyz(n)
print(c)