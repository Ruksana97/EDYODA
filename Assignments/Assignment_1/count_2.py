numbers=eval(input('Enter the series of numbers: '))
count_even=0
count_odd=0
i=0
while i<len(numbers):
    if numbers[i]%2==0:
        count_even+=1
        i=i+1
    else:
        count_odd+=1
        i=i+1
print('Number of odd numbers are',count_odd)
print('Number of even numbers are',count_even)