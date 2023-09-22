# Tool to visualize what computer is doing step-by-step as it executes the said program:

def test(computer_a):
    def add(computer_b):
        nonlocal computer_a
        computer_a += 1
        return computer_a + computer_b
    return add
func = test(4)
print(func(4))
    