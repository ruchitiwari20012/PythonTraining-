def function1():
    print("Subscribe now")
func2 = function1
del function1
func2()

#function1 after deleting also run bcoz the copy 
# is created in func2

