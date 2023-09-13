dict_1 = {"ki":200, "k2": 400, "k3": 600, "x1": 240, "lou": 457, "ab": "whatever"}


for idx, (key, value) in enumerate( dict_1.items( ), 1 ):
    eol_char = "\n" if idx % 3 == 0 else ""
    print(f'{key =} {value = } ', end=eol_char)
# Sort the Dictonary....
    print("Sorted...")
    for idx, (key, value) in enumerate (sorted(dict_1.items( )), 1 ):
        eol_char =
        print(f'{key =} {value =} {( eol_char := chr(10) if idx % 3 == 0 else "")}', end=eol_char)