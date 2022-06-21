''' 
    A class defines a set of attributes that are shared across instances of that class.
    -----------------------------------------------------------------------------------
    +++++++++  classes are sets of functions, variables, and properties ++++++++++++
    ----------------------------____---------------------------------____--------------
'''

class Employee(object):
    # initial number 
    numEmployee = 0
    # Set the initial properties of the class Employee
    def __init__(self, name, rate) -> None:
        self.owned = 0
        self.name = name
        self.rate = rate
        # in the case of a new Employee, increase the number of Employee
        Employee.numEmployee +=1 
        
    # Defined a delet method for decrement of numbers of Employee
    def __del___(self):
        Employee.numEmployee -= 1
        
    ''' Calculate the working hour and rate[ performance of an Emploee] '''
    # Eval the working hour 
    def hour(self, numHours):
        # calling the set initial of the class self.owned as the number[default value] of working hours
        # add the owned hour to the parameter numHours in the hour function  
        self.owned += numHours + self.rate
        return f'{numHours} hours worked'
    
    # calculate the Employee pay
    def pay(self):
        self.owned = 0
        return f'payed {self.name}'
    
    
''' Let's create an instance of an Employee Class '''
# create employee 
employee1 = Employee('codingGee', 90)
employee2 = Employee('Sam Archibong', 80.5)

''' employees number '''
emp_num1 = employee1.numEmployee
emp_num2 = employee2.numEmployee
''' get working hours '''
emp_hrs = employee1.hour(10)
emp_hrs2 = employee2.hour(9)

''' employ owned'''
emp_owned = employee1.owned
emp_owned2 = employee2.owned

''' pay employee '''
emp_pay = employee1.pay()
emp_pay2 = employee2.pay()

# prints all the information of employees
# print(f'Total Employees: {Employee.numEmployee}')
# print(f'The employer {employee1.name} has work rating of {emp_hrs}, his pay is: $ {emp_owned} per day, per month: $ {emp_owned * 31} per month and: ${emp_owned * 365}' )
# print(emp_pay)
# print(f'The employer {employee2.name} has work rating of {emp_hrs2}, his pay is: $ {emp_owned2} per day, per month: $ {emp_owned2 * 30} per month and: ${emp_owned2* 365} ')
# print(emp_pay2)


''' inheritance "new class that modifies the behavior of an existing class through" '''
# inheriting properties of a class
class SpecialEmployee(Employee):
    ''' For a subclass to define new class variables, it needs to define an __init__() method '''
    #caling the parent initial vals
    def __init__(self, name, rate, bonus) -> None:
        super().__init__(name, rate)
        self.bonus = bonus
    
    # inherit from the base class
    def hours(self, numHours):
        self.owned += numHours * self.rate + self.bonus
        return f'{numHours} hours worked'
    
print(isinstance(SpecialEmployee, Employee))

''' Class method '''
class Aexp(object):
    base = 2
    @classmethod
    def exp(cls, x):
        return (cls.base**x)
    
class Bexp(Aexp):
    base = 3
    
