
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



class Employee:
    def __init__(self, id, name, salary):
        self._id = id
        self._name = name
        self.salary = salary
    
    # Decorators that define PROPERTIES
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, new_sal):
        # Business Rule: salary between 30k and 200k
        if 30_000 <= new_sal <= 200_000:
            self._salary = new_sal
        else:
            raise ValueError(f"New value of salary, {new_sal}, outside allowable range")
        
an_employee = Employee(123, "Pete Moss", 2_135_234.56)
# Where's the Value error?
print(f'Employee Salary: {an_employee.salary}')

    

