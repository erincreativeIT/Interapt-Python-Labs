
#Part 1: Aritmetic operators 

an_int = 100
another_int = 200
a_float = 2.71828
another_float = 3.14159
#an_int is a whole number, a_float is a decimal number the first part is the whole number * the decimal 
#thhe second part is stating the whole number times the decimal.
#all of the yellow is a string what is in the curly brackets is what the code will equate 
print( f'{an_int} times {a_float} = {an_int * a_float}')
print( f'{an_int} divided by {a_float} = {an_int / a_float}')
#This is the Eulcer's Identity equation ** is the same as ^
print( f' {a_float} raised to the power of {another_float}'
#:.6f will make it where only 6 decimals will show and this part on the line will show the answer to the equation
       f'to 6 decimals is {a_float ** another_float:.6f}') 
# the directions are saying you have to do 100 + 200= 300 THEN * you CANNOT do it all at once 
print( f'{an_int} plus {another_int} THEN multiplied by {a_float}'
       f'is {(an_int + another_int) * a_float }')
# without the f' this runs as a regular string
print('{an_int} plus {another_int} THEN divide by {a_float} plus '
      '{another_float} is {(an_int+another_int)/(a_float+another_float)}')
print( f' {an_int} divided by {a_float} plus {another_int} divided by {another_float} '
      #below will show is then the answer to the equation
       f'is {an_int/a_float + another_int/another_float}') 
print()
#Part 2: Compare and logical operators
#Use the same values as in part 1
#the operator is what is letting it know that you want to find out if it's true or false
print( f'Is {an_int} less than {another_int}? {an_int <another_int}')
print( f'Is {an_int} greater than {a_float} OR {another_float} equal to {another_int}? '
#the or is ignored in this case and it is true because if anything is true the whole thing is true
       f'{an_int > a_float or another_float == another_int}')
print( f'Is {an_int} cubed greater than {another_int} squared?'
       f'{an_int ** 3 > another_int **2}')
print( f'Is true greater than false? {True > False}')
print()
# Identity operators
num1 = 100
num2 = 100.00
print( f'{num1} equals {num2} ? {num1 == num2}')
print( f'{num1} is the same object as {num2} ? {num1 is num2}')
# Part 2: Convert from Celsios to Fahrenheit
#No error checking done here for invalid inputs
cels_convert = float( input( "Enter a Celsuis temperature ==> "))
print( f'Fahrenheit equivalent is { ( ( 9 * cels_convert) / 5 ) + 32}')

