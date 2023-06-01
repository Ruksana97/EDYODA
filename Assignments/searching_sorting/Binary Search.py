def Binary_Search(array,key):
    high=len(array)-1
    low=0
    mid=0
    while low<=high:
        mid=(high+low)//2
        if array[mid]<key:
            low=mid+1
        elif array[mid]>key:
            high=mid-1
        else:
            return mid
    return -1

array=[int(i) for i in input().split()]
key=int(input('Enter the value to be searched:'))
ans=Binary_Search(array,key)
if ans!=-1:
    print('Element found at index:',ans)
else:
    print('Element not found')