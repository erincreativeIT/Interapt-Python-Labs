#Count lower-case vowels in input string, enter <enter> to quit
vowel_count = 0

vowel_list = 'aeiou'

 

 

while True:  
 vowel_count = 0
 
 my_string = input("Enter an input string, enter <enter> to quit: ")
 if my_string == '':
        break
my_string = my_string.lower()
for a_char in my_string:
    if a_char in vowel_list:
        vowel_count += 1
            
print(f'Vowel count of :{my_string} = {vowel_count}')