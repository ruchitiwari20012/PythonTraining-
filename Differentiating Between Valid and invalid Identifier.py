import re

#Making a regular expression for valid identifier
regex = '^[A-Za-z_][A-Za-z0-9]*'

#Defining a function
def check(string):

#Passing the regular expression  and the string in search() method
   if (re.search(regex,string)):
       print('Valid Identifier')

   else:
        print('Invalid Identifier')

        #Driver Code
if __name__ == '__main__' :
       
       #Enter the enter string
       string = 'ftf'

       #Calling run function
       check(string)
       
       string = "123"
       check(string)

       string = '#abc'
       check(string)