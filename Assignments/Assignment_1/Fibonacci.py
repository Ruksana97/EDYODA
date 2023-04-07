num=int(input('Enter the limit for Fibonacci series: '))
last_num=0
sec_last=1

for i in range(0,num):
    if i==0:
        sum=0
        print(sum, end=" ")
    else:
        sum=sec_last+last_num
        sec_last=last_num
        last_num=sum
        if sum<=num:
          print(sum,end=" ")


