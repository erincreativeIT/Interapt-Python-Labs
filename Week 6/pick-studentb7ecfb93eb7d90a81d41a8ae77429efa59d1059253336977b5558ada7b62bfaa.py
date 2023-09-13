import random
# Pick a student name at random
students = "Erin Ashley Janira Shaq Seiku Nate Leo Val Laura Debbie Jordan".split(" ")

while(len(students) > 0):
    random.shuffle(students)
    a_student = students.pop()
    print(f'Selected student: {a_student}')
    _ = input("Press <enter> to select next student...")
    
print('All selected')
    