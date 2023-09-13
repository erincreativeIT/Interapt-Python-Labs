def one_arg(arg):
    pass

def func_vary(**dict_arg):
    print(f'Number of OPTIONAL args passed to func_vary = {len(dict_arg)}')
    print(f'Arg looks like: {dict_arg}' )

def func_req_vary(pos_arg, **dict_arg):
    print(f'Positional arg: {pos_arg}')
    print(f'Number of OPTIONAL args passed to func_vary = {len(dict_arg)}')
    print(f'Arg looks like: {dict_arg}')
# { "arg1", {arg1:"Lou", arg2=235, arg3=[1,2,3]}}

# No arguements required here
func_vary()
#How about this?
func_vary(arg1="Lou", arg2=235, arg3=[1,2,3])
# May use positional before varying keyword
dict_ = dict(arg1="Lou", arg2=235, arg3=[1,2,3])
one_arg(dict_)

func_req_vary( 100, arg=dict_)

func_req_vary( 100, arg1="Lou", arg2=235, arg3=[1,2,3])