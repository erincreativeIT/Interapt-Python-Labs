def create():
    print("Gonna add")

def read():
    print("Gonna read")

def update():
    print("Gonna update")

def delete():
    print("Gonna delete")

option: str = input("Enter c, r, u, d ==> ")
func_dict = {'c': create, 'r': read, 'u': update, 'd': delete}

func_dict[option]() #r ==> read

