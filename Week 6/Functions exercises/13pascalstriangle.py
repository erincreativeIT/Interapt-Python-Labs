# Write function that prints out the first n rows in Pascal's triangle

def pascal_triangle(num):
    trow = [1]
    y = [0] #normally name this but I do not know what y is in this case
    for int in range(max(num, 0)):
        print(trow)
        trow = [1 + row for list, row in zip(trow+y, y+trow)]
    return num >= 1
print(pascal_triangle(6))