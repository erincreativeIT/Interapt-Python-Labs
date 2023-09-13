import random

# Make a list out of the student names written 
student_list = "Erin Ashley Janira Shaq Seiku Nate Leo Val Laura Debbie Jordan".split()
print(student_list)

for name in student_list:
    #Use 'name' as the random selection from the list
    ...
   #print(f"Student selected is {name}"")
   #student_list.pop()
   # print("Press <enter>"
while len(student_list) > 0: #truthy/falsy while student_list: 
    #Shuffle List
    random.shuffle(student_list)
    #Return AND REMOVE an element (and print it as well)
    #selected_name = student_list.pop()
    # print(f'Selected student: {selected_name} ')
    print(f'Selected student: {student_list.pop()}')
    s_input = input("Enter <enter> to get annddah name")

print("All done")
    # Return AND REMOVE an element (and print it as well)
    # selected_name = student_list.pop()
    #print(f'Selected student: {selected_name} ')
  # Pause program allow user to press <enter> to get next name

    
    
#
#random.shuffle(a_list)
# an elem = a_list.pop()

#Many ways to do random selection in Python. We'll chohose one.
#
#Shuffle your list using a function in the random module (look it up)