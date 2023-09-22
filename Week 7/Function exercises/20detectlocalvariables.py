# Write a program to detect the numver of local variables declared in a functino
def abc():
    num1 = 1
    num2 = 2
    str1= "w3resource"
    print("Python Exercises")

print(abc.__code__.co_nlocals)