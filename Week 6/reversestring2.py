#reverse string slice method

string = "1234abcd"

def reverse_string(my_str):

    for a_char in my_str[::-1]:
        print(a_char, end='')


# function call with string passed an arg
reverse_string(string)