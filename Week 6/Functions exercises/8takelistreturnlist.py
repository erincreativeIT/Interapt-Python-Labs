# Write a Python function that takes a list and returns a new list with distinct 
#Elements from the first list

def unique_list(list):
    new_list = []
    for num in list: #it will return new list and will only have 3 once
        if num not in new_list: #it will replace all the other numvers and only have 6
            new_list.append(num)
    return new_list

print(unique_list([1,2,3,3,3,3,4,5]))