# a factorial is calulated by multipling the whole numbers from the choosen
# Number down to 1

non_negative = 0

def factorial(non_negative):
    if non_negative == 0:
        return 1
    else:
        return non_negative * factorial(non_negative-1)
        

non_negative = int(input("Input a number to compute the factioral: "))
print(factorial(non_negative))
