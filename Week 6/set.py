int_1 = 1_000
int_2 = int_1
print(f'Are these the same object? {int_1 is int_2}')
int_2 = 2_000

exit()


set_1 = {1, 2, "a", "b", 4}
set_2 = set_1
print(f'Are these the same object? {set_1 is set_2}')
set_2.add(1_000_000)
print(f'After set_2 changes, are these the same object? {set_1 is set_2}')
print(f'Note set 1 changed but didnt add elem to it: {set_1 = } ')

set_3 = set_1.copy()
print(f'Are 1, 3 thhe same object? {set_1 is set_3}')
set_1.add("Lou")
print(f"Does set_3 change? {set_3 = }")
