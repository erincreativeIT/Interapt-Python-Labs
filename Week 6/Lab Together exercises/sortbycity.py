one_state_data = {"Austin": 950000, "San Antonio": 1345678,
                  "Dallas": 1112222, "Houston": 4111222 }
# Sort by key - default
print("Sorted by city name")
for item, value in sorted(one_state_data.items ( )):
    # sorted: [ (Austin, 999), ("san a", 34354325), ..., ("Dallas"), 65436 ]
    print( f'key = {item}\tValue={value}')
print()
# Use lambda to sort by value
print("Sorted by population")
for item, value in sorted ( one_state_data.items( ), key=lambda pair: pair[ 1 ]):
    print(f'Key = {item}\tValue={value}')

exit()