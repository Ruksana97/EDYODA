class Count_of_Pairs():

    def __init__(self,*data):
        self.array=list(data)



    def Count_Pair(self,sum):
          n = len(self.array)
          count= 0
          for i in range(0, n):
             for j in range(i + 1,n):
               if self.array[i] + self.array[j] == sum:
                   count+= 1

          return count

x=Count_of_Pairs(1,2,3,4,5)


sum=7
x.Count_Pair(sum)
print('Total pairs that gives',sum,'is :',x.Count_Pair(sum))
