def func_vary ( *several_args ):
    print(f'Arg type in func_vary: {type(several_args)}')
    print(f'Number of args passed to func_vary = {len( several_args )}')

    for idx, an_arg in enumerate(several_args, 1):
        #Do something with an arg
        print(f'Arg number {idx} is {an_arg}')

def func_one( one_arg ):
    print(f'Arg type in func_vary: {type(one_arg)}')
    print(f'Number of args passed to func_one = {len( one_arg )}')
#pass 0 args....
#func_vary( )
#How about 1...
func_vary( 1, 2, 3, "Yo", "No")
# May pass a tuple (or anything) as a single argument
func_one( (1,2,3,4,5) )