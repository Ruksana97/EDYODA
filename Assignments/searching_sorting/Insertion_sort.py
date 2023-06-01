def Insertion_sort(array):
    n=len(array)
    for i in range(1,n):
        temp=array[i]
        j=i-1
        while j>=0 and temp<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=temp
    return array

print(Insertion_sort([3,54,9,23,6,43]))

