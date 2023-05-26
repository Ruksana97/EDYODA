class Sum:
    def __init__(self):
        self.array=[1,2,3,4,5]

    def sum(self,data):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1):
              if self.array[i]+self.array[j+1]==data:
                  print((self.array[i],self.array[j+1]) )

x=Sum()
x.sum(7)




