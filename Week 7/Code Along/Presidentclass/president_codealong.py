'''
Create a module named president that implements a President class. This
class has a CTOR that takes the index number of the president (1-44) and creates
an object containing the associated information from the presidents.txt file.
Provide the following properties (types indicated after -->):
term_number --> int
last_name --> string
first_name --> string
birth_date --> date object
death_date --> date object (or None, if still alive)
birth_place --> string
birth_state --> string
term_start_date --> date object
term_end_date --> date object (or None, if still in office)
party --> string
The CTOR takes a single argument: The term number of a president.
'''


class President:
    def __init__(self, term_num):
        with open("presidents.txt", "r") as file:
            for a_pres_data in file:
                fld_list = a_pres_data.split(":")
                print(f'{fld_list = }')
                if term_num == int(fld_list[0]):
                    self._term_num = term_num
                    self._last_name = fld_list[1]
                    self._first_name = fld_list[2]
                    self._birth_date = fld_list[3]
                    self._death_name = fld_list[4]
                    self._birth_place = fld_list[5]
                    self._birth_state = fld_list[6]
                    self._term_start_date = fld_list[7]
                    self._term_end_date = fld_list[8]
                    self._party = fld_list[9]

                    break
@property
def term_num(self):
    return self._term_num

property
def first_name(self):
    return self._first_name

property
def last_name(self):
    return self._last_name
property
def birth_place(self):
    return self._birth_place

property
def birth_state(self):
    return self._birth_state

property
def birth_date(self):
    return self._birth_date


# string.split(delim)
# 7 Jackson Andrew 1767-03-15 1845-06-08 Waxhaw South Carolina  182
# id_list[0] == 7