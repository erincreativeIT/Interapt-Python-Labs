def string_count_test(string):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for count in string:
        if count.isupper():
            #This adds the amount of upper to the count
            d["UPPER_CASE"]+=1
            #This adds the amount of lower to the count
        elif count.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("Original String : ", string)
    print("No. of Upper case characters: ", d["UPPER_CASE"])
    print("No. of lower case characters: ", d["LOWER_CASE"])

string_count_test('I am Violet Creative I know who you are. I know you can hear me')