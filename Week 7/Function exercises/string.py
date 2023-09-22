# Write a python code to execute a string containing Python code

mycode = 'print("Hello World")'
code = """
def multiply(num1, num2):
    return num1*num2

print('Multiply of 2 and 3 is: ' ,multiply(2,3))
"""

exec(mycode)
exec(code)
