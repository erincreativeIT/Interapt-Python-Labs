

def perfect_number(num):
    sum = 0
    for integer in range(1, num):
        if num % integer == 0:
         sum += integer
    return sum == num
print(perfect_number(6))