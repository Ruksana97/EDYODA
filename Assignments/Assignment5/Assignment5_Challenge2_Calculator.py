class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print(self.num2+self.num1)


    def subtract(self):
        print (self.num2- self.num1)

    def multiply(self):
        print(self.num2 * self.num1)

    def divide(self):
        try:
            print(self.num2/self.num1)
        except ZeroDivisionError :
            print("Denominator cannot be zero")
            #raise ZeroDivisionError

obj=Calculator(10,94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()

