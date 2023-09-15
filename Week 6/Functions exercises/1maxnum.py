# return max num of three numbers

#max_num = []
#def is a function

def max_number(num_list):

    max_num = 0

    for num in num_list:
        if num > max_num:
            max_num = num

    return max_num
# this will return an integar 
the_max = max_number([3, 5, 7, 9 ,2, 100])

f_string = 'program complete'

print (f'Max num ==> {the_max} so {f_string}')