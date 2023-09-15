# Write a function that checks if a number is prime or not

def is_prime(candidate):
   for num in range(2, candidate):
      # if candidate divided by num equals 0
      if candidate % num == 0:
         return False
      
   return True 
print(is_prime(9))