import random

#Find common elements for a pair of iterators 
def find_common_unique_elements( iter1, iter2 ):
    list_with_common = []
        #list_with_common = [elem for elem in start if elem in iter2 and elem not in list_with_common] 
        #Do something here to fill up the list
    for iter1_elem in iter1:
        if iter1_elem in iter2 and iter1_elem not in list_with_common:
            list_with_common.append( iter1_elem )



    return list_with_common
#This function calls the above for two lists 
#We check if we have at least two lists
def find_common_elems_buncha_iters( buncha_iters ):
     # Need to know HOW MANY LISTS we have

     # Pass first two iterables; save common elements 
     # How do we access the first two elements of the buncha_iters structure?
      # Need an expression that ITERATES OVER REMAINING LISTS IN buncha_iters
    common_elems = find_common_unique_elements( buncha_iters[ 0 ] ,
                                                buncha_iters[ 1 ] )
    # In the block coded above, call find_common_unique_elements with arguments
    # common_elems and the NEXT LIST in the remaining lists in buncha_iters
    #   = find_common_unique_elements( common_elems,  )

    # When done, this has ALL the common elements
    return common_elems 

# Generate and return a random list of num_items items
# Each integer between 0 and 15
def gen_return_random_num_list( num_items ) :
    return [ random.randint(0, 20) for _ in range(0, num_items) ] 

def main( ):
    num_iterators = int( input( "Enter number of iterators (5-10) ==> "))
    num_each_iterator = int(input("Enter number for each iterator (15-20) ==> "))
    #Create buncha_iterator structure 
    buncha_iters = [ gen_return_random_num_list( num_each_iterator )
                                   for _ in range(0, num_iterators ) ]
        # Print the buncha_iters generated
        # Maybe make the output a bit easier to read???
    for an_iter in buncha_iters:
        print(f'{sorted( an_iter)}')

        #OK - let's print out the common elements
        print(f'Elements common to all list: {find_common_elems_buncha_iters( buncha_iters) }')

main()
