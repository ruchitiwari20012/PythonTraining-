import datetime
x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2021, 11, 1)
print(x.strftime("%B"))