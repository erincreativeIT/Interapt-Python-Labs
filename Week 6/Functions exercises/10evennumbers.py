# Print the even numbers from the given list

def even_number(list):
    enum = []
    for num in list:  #have to have for first to state its # in list
        if num % 2 == 0:
            enum.append(num) # will take out all odd numbers
    return enum

print(even_number([1,2,3,4,5,6,7,8,9,10]))
