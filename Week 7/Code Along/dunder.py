class MagicMethods:
    # __init__ omitted to save room here

    # Print a representation of an Employee object using magic method override
    def __str__(self):
        return (f"Info for Employee with ID =  {self._empID}\n"
                f'Name: {self._empName}\tDepartment code: {self._empDept}\t'
                f'Salary: {self._empSalary:,.2f}\n')

    # Two employees are equal iff they are in the same department
    def __eq__(self, rho):
        return self._empDept == rho._empDept
    
    # Emp1 > Emp2 iff Emp1 salary > Emp2 salary
    def __gt__(self, rho):
         return self._empSalary > rho._empSalary
    
    # Look for value in any object field (overrides 'in' operator)
    def __contains__(self, item):
        return item in (self._empID, self._empDept, self._empSalary, self._empName)


if __name__ == "__main__":
    emps = [MagicMethods("Lou", "D11", 123_456), MagicMethods("Joe", "E11", 473_456),
            MagicMethods("Sue", "D11", 98_456), MagicMethods("Pam", "F11", 233_456)]
        # Call magic methods via operators
    print( f"Are 'Lou' and 'Joe' equal? {emps[0] == emps[1]}")
    print( f"Are 'Lou' and 'Sue' equal? {emps[0] == emps[2]}")
        # Are any employeess named "pam":
    for an_emp in emps:
            if "Pam" in an_emp:
                print(f"'Pam' found in:\n{an_emp}")
        #Find the 'largest' userEmployee
    print(f'The "largest" employee is :\n{max(emps)}')

