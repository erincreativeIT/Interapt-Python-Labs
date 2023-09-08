# name = input("Emter your name ==> ")
# print("name =" , name)
#print(f'I am {name} ')

name = input("Enter your name ==>")
print("name =", name)
print(f'I am {name} ')
print(f'I am \n\t{name}\n and I are coding ')
print()

#import commandline arguments 
import sys
#This is allowing us to feed a prompt and isolate the things that we feed it. sys.argv is built into the module
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
print(f'sum of {num1} and {num2} is {num1 + num2}')

