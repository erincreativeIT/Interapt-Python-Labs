from random import randint


# Find elements common to two lists
# this will be used to find common llist elements to > 2 list later on.
# For now, lets just do two of them

#Get the number of elements for both list; ask for a number between 10 and 20


num_in_list = int(input("Enter a number between 10 and 20 ==> "))

# Generate a list of num_in_list random integers between 1 and num_in_list
# Remember the range function includes the lower bound (0, in this case)
#and excludes the upper bound (num_in_list, in this case)
# the one below is simliar to line 21 and 24 but is closer to Java Script 21 and 24 is how you write in python.
list_1 = []
for i in range(num_in_list):
    list_1.append(randint(num_in_list))

list_1 = [ randint(1, num_in_list) for i in range( num_in_list) ]

# Generate another list of num_in_list random integar between 1 and num_in_list
list_2 = [randint(1, num_in_list) for i in range(num_in_list) ]

print(f'{list_1}\n{list_2}')


#Find common elements for pair of iterators. Do not include duplicates
#Lets try this


# Initialize an empty list to hold the common elements 
common_elems = [] # list() works, too
#iterate over elements of list_1 (doesn't matter which list we start with)
for element in list_1:
    # Inside the loop, deteremine if the element in list_1 is in list_2 AND
    # we did not already find this element. If so, add the element 
    #to the list of common elements. If not, do nothing.
    if element in list_2 and element not in common_elems:
        common_elems.append(element)

#print a sorted verison of both list and the list of common elements
list_1.sort()
list_2.sort()
print(f'{list_1}\n{list_2}\n\n{common_elems}')


