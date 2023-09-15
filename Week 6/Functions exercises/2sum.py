
#this is the list I am finding the sum of
num_list = [8, 2, 3, 0, 7] # This is argument
#def_sum is the function name
# passing the list to find_sum in the for loop
def find_sum(num_list): #num_list is the perameter
    # for each num in list do this 8 will pass through first
    # the intial value is to have a base point, 8 is going to add to this which is 0 
    sum_of_list = 0 #This variable is going to change 
    for num in num_list:
        sum_of_list = sum_of_list + num
        # this will return when list is complete
    return sum_of_list
#list_sum = find_sum([8, 2, 3, 0, 7])
print(find_sum(num_list)) # pass in num_list and find sum will take this as an argument and do the equation
        
#print(find_sum((8, 2, 3, 0, 7)))- this is a tuple which also works 
