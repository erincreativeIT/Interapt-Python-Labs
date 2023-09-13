# Create dictonary using shorthand
dict_1 = {"k1" :200, "k2" : 400, "k3" : 600}
list_1 = ['a', 'b', 'c']
tup_1 = tuple(range(1,4))
#The zip() function creates an iterable of tuples and extra K/V pairs
dict_zip = dict( zip(list_1, tup_1), anothKey = "AnothVal" )
# {'a' : 1, 'b' : 2, 'c' : 3, anothKey= "anothValue"}
#What's this look like when printed?
print(f'Shorthand dictinary {dict_1 = }')
print(f'Dictonary from zip() iterable {dict_zip = }')
#Notice the zip() iterable doesn't have a clearn, printable form
print(f'Zip object: {list(zip(list_1, tup_1 ))}')