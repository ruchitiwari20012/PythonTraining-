from functools import reduce

list1 = [1,2,3,4,7]
num = reduce(lambda x,y: x+y, list1)
print(num)

#these help in performance and syntx reduce.