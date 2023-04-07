numbers=eval(input('Enter the series of number: '))
count_even=0
count_odd=0
for i in numbers:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print('Number of odd numbers are',count_odd)
print('Number of even numbers are',count_even)