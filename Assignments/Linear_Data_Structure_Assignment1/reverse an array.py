class Reverse_an_array:
    def __init__(self,*args):
        self.array= list(args)

    def reverse(self):
        self.array = self.array[::-1]
        return self.array

x=Reverse_an_array(2,3,4,5)
print(x.reverse())


