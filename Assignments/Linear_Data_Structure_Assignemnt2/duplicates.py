class find_duplicate:
    def __init__(self,*data):
        self.array=list(data)

    def duplicate(self):
        duplicate_array= []
        for i in range(len(self.array)):
           if self.array.count(self.array[i])>1 and self.array[i] not in duplicate_array:

             duplicate_array.append(self.array[i])
        return duplicate_array




x=find_duplicate(1,3,4,1,5,3,2)

print(x.duplicate())
