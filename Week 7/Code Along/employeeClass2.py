#Code a class that models employees that:
    #Has 4 fields: empID, empName, empDept, empSalary
    #All fieldss initalized in CTDR
    # empSalary must be between 30K and 200K
    # If outside this range, a diagnostic is printed
    #Values outside this range force empSalary to None
    # This class has two methods:
    # print_me, which prints the values of all the fields
    #give_emp_pct_raise, which takes an arg represnting a percent raise for the employee
    # The arg must be between 10 and 20
    #If outside this range, a diagnostic is printed
    # If after the raise calcuation the salary exceeds 200K, the salary is set to 200K
    # If the employee does not have a valid salary (set to None in the setter, perhaps), print 
    # diagnostic 

class EmployeeWMethods:
    def __init__(self, empID, empName, empDept, empSalary):
        # _ is a signal to never access this directly (true encapsulation) python can't do this the programmer has to
        self._empID = empID
        self._empName = empName
        self._empDept = empDept
        self._empSalary = empSalary
# Jusst one property- wanna keep this short
    @property
    def empSalary(self):
        return self._empSalary
   
    @empSalary.setter
    def empSalary(self, new_val):
        self._empSalary = None
        if 30_000 <= new_val <= 200_000:
            self._empSalary = new_val
        else:
            print(f"Passs value of {new_val} not in range. Salary is set to 'None'")
            self._empSalary = None

            # different way to code the if statement below 

            #if new_salary < 30_000 or new_salary > 200_000:
             #   print(f"Pass value of {new_salary} not in range. Salary set to 'None'")
               # self._emp_slary = None
           # else:
              #  self._emp_salary = new_salary

    def give_emp_pct_raise(self, pct_raise):
        if self._empSalary is None:
         print(f'Employee with ID = {self._empID} has no valid salary - no change made ')
        elif pct_raise < 10 or pct_raise > 20:
         print(f'Raise percentage {pct_raise} out of range - no change made ')
        else:
            self._empSalary *= (1 + pct_raise/100)
            if self._empSalary > 200_000:
                self._empSalary = 200_000

    def print_me(self):
        print(f"Info for Employee with ID = {self._empID}")
        print(f'Name: {self._empName}\tDepartment: {self._empDept}\tSalary: {self._empSalary:,.2f}')

  #  if self._emp_salary is None:
   #   print(f'Employee with ID = {self._emp_ID} has no valid salary - no charge mode')
  #  elif 10 < pct_raise < 20:
   #   self._emp_Salary = self._emp_Salary * (1 + pct_raise/100)
  #    if self._emp_Salary > 200_000:
    #        self._emp_Salary = 200_000
   # else:
     # print 
if __name__ == "__main__":
    an_emp = EmployeeWMethods(123, "Lou", "D11", 123_456)
    #Print Employee salary
    print (f'From Class: {an_emp.empSalary = }')
    # Give raisse, print again
    an_emp.give_emp_pct_raise(20)
    print(f'From class: {an_emp.empSalary = } ')
    print(f'{an_emp.empSalary}')
    # Print employee particulars
    an_emp.print_me()

            
        

