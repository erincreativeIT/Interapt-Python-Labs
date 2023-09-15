import math
numbers = list( range( 1, 5) )
print(f'original list: {numbers}')

 


# Generate multiple values - a list of tuples
root_table = [ ((num, math.pow(num,.5), math.pow(num, 1/3)) ) for num in numbers
         if math.pow(num,.5) > 1.4]

# [ (1, 1, 1), (2, 1.41426, dfa), (3, 1.7something, jfjfj;), (4, 2, kjfav) ]
for num, sqrt, cubert in root_table:
     print(f'{num: <5d}\t\t{sqrt:<.3f}\t\t{cubert:<.3f}')

   

for tup_vals in root_table:
    print(f'{tup_vals[0]: <5d}\t\t{tup_vals[1]:<.3f}\t\t{tup_vals[2]:<.3f}')

root_table = []
for num in numbers:  
    root_table.append( (num, sqrt:=math.pow(num,.5), cubert:=math.pow(num, 1/3)) )
print(f'{num: <5d}\t\t{sqrt:<.3f}\t\t{cubert:<.3f}')

for num, sqrt, cubert in root_table:      
     print(f'{num: <5d}\t\t{sqrt:<.3f}\t\t{cubert:<.3f}')

exit()  

# May nest list comprehensions

suits = ('Clubs','Diamonds','Hearts','Spades')
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
deck = [ (rank,suit) for suit in suits for rank in ranks ]

for rank,suit in deck:
     print(f"{rank= }\t\t{suit= }")

 