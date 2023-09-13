# Enter a string, count the lower case vowels. enter <ith some vowelsenter> to quit

vowels = "aeiou"
while True:
    count_me = input("Enter a string or <enter> to quit ==> ")
    if len(count_me) == 0:
        break
    lc_vowel_count = 0
    for a_char in vowels:
        lc_vowel_count += count_me.count(a_char)

       
    print(f'Vowel count in "{count_me}" is {lc_vowel_count}')

   

print("All done!")