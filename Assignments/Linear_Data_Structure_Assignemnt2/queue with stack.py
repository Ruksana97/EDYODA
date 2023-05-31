class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enQueue(self, num):

        
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()


        self.stack1.append(num)


        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            print(self.stack2)
            self.stack2.pop()


    def deQueue(self):


        if len(self.stack1) == 0:
            print("Q is Empty")


        x = self.stack1[-1]
        self.stack1.pop()
        return x



y = Queue()
y.enQueue(1)
y.enQueue(2)
y.enQueue(3)

print(y.deQueue())
print(y.deQueue())
print(y.deQueue())