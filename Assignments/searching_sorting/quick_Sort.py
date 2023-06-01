def quick_sort(array):

    if len(array)<1:
        return array
    else:
        pivot=array.pop()


    greatest=[]
    smallest=[]
    for i in array:
        if pivot<i:
            greatest.append(i)
        else:
            smallest.append(i)
    return quick_sort(smallest)+[pivot]+quick_sort(greatest)

print(quick_sort([5,33,76,1,4,90,47]))