class Move_negative_elements:
    def __init__(self,*data):
        self.array=list(data)

    def shift(self):
        x=self.array.sort()
        for i in self.array:
            print(i,end=" ")
        return

list1=Move_negative_elements(2,-4,-2,6)
list1.shift()

