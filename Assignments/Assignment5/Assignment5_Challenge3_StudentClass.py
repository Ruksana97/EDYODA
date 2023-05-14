class Student:

    def setName(self,x):
        self.__name=x

    def getName(self):
        return self.__name

    def setRollNumber(self,y):
        self.__rollno=y
    def getRollNumber(self):
        return self.__rollno

a=Student()
a.setName(input('Enter the name:'))

a.setRollNumber(int(input('Enter the rollno:')))
print(a.getName())
print(a.getRollNumber())