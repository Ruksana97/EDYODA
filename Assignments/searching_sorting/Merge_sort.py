def merge_sort(array):
    if len(array)<2:
        return array

    mid=len(array)//2
    print(mid)
    left=merge_sort(array[:mid])
    right=merge_sort(array[mid:])
    print(right)
    return merge(left,right)

def merge(left,right):
    result=[]
    i=0
    j=0
    while len(left)>i or len(right)>j:
        if (left[i]<right[j]):
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
        if len(left)==i or len(right)==j:
            result.extend(left[i:] or right[j:])
            break
        return result
print(merge_sort([10,42,1,5,67,23,50]))

