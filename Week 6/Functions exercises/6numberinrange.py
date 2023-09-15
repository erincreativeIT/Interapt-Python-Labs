# check whether a number falls within a given range
def test_range(num):
    if num in range(3, 9):
        print( " %s is in the range" %str(num))
    else:
        print("The number is outside the given range.")
    
test_range(5)
test_range(10)
test_range(2)
test_range(4)