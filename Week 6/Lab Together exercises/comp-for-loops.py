# Write these loops as scomprehensions

# Create a list of the first 10 numbers 
first_ten = [0,1,2,3,4,5,6,7,8,9]
rfirst_ten = list(range(0,10))

new_list = [] #[0, 1, 4]
for num in first_ten:
    new_list.append(num ** num)

    # As a comprehhension....

new_list = [num ** num for num in first_ten]

new_list = []
for num in first_ten:
     if num > 3:
         new_list.append(num * 2)



# As a comprehension
new_list = [num * 2 for num in first_ten if num > 3]

