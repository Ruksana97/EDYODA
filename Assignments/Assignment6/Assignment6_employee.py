import json


class Employee:
    def __init__(self):
        self.employee={}
        self.employee_id=len(self.employee)+1
    def add_employee(self):
        self.name=input('Enter the name of the employee:')
        self.dob=(input('Enter the Date of Birth of the employee:'))
        self.height=float(input('Enter the height of the employee in centimeters:'))
        self.city=input('Enter the City of the employee:')
        self.state=input('Enter the state of the employee:')
        self.employee_details={'Name':self.name,'Date_of Birth':self.dob,'Height':self.height,'City':self.city,'State':self.state}
        self.employee_id = len(self.employee) + 1
        self.employee[self.employee_id]=self.employee_details
        with open('employee.json', 'w') as f:
            json.dump(self.employee, f)
            print('information added successfully')

x=Employee()
x.add_employee()

x.add_employee()


x.add_employee()


