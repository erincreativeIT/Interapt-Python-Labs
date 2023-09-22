# Enter an expression containing numbers and the 'usual' arithmetic operators
# For now, don't use parenthesis and don't worry about zerodivides
# Parse the expression and call functions to perform the arithmetic
# Let's make it a bit easier - put at least one space between numbers and operands
#


# Now, put in add, mul, etc.
# lambda x,y: x + y
def add(x,y):
    return x + y   

def sub(x,y):
    return x - y   

def mul(x,y):
    return x * y   

def div(x,y):
    return x / y      #     45 + 345

# Create a dictionary using operators as keys, functions as values
operators = {"+": add, "-": sub, "*": mul, "/": div}   
# Get an expression num1 op num2 from user, blank-delimited
lho, operator, rho = input("Enter an expression num1 op num2 from user, blank-delimited ==> ").split()
# Check if operator (key) in operators dictionary
try:
    lho = float(lho)   # LHO
    # operator = express_list[1]
    rho = float(rho)   # RHO

    # Call/print function using dictionary of functions
    # operators = {"+": add, "-": sub, "*": mul, "/": div}
    calc_result = operators[ operator](lho, rho)
    print(f'Result of {lho} {operator} {rho} is {calc_result}') 
except KeyError as ke:
    operators_as_list = list(operators.keys())
    print( f"operator {operator} entered not in {','.join(operators_as_list)}" )






if operator in operators:
    # Get lho, operator, rho from user input expression
    # express_list   = expression.split()
    # express_list[0] ==> lho  (STRINGS!!!!!!!!!!!!!!!!!!!)

    # lho, operator, rho = expression.split()

    # Convert numeric strings into 'real' numbers (use 'float' not 'int' unless problem states
    # input HAS TO BE an int)
    lho = float(lho)   # LHO
    # operator = express_list[1]
    rho = float(rho)   # RHO

    # Call/print function using dictionary of functions
    # operators = {"+": add, "-": sub, "*": mul, "/": div}
    calc_result = operators[ operator](lho, rho)
    print(f'Result of {lho} {operator} {rho} is {calc_result}')
else:
    operators_as_list = list(operators.keys())
    print( f"operator {operator} entered not in {','.join(operators_as_list)}" )    
    
    # Change this:   dict_keys(['+', '-', '*', '/'])
    # to this        ['+', '-', '*', '/']
    
    # to this        '+,-,*,/'
                   