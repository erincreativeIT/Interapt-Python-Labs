num_list = [8,2,3,-1,7]

def find_times(num_list):
    
    times_of_list = 1
    for num in num_list:
        times_of_list = times_of_list * num
    return times_of_list
    
print(find_times(num_list))
    


    