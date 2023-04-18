def add(*a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum


print(add(8,2,3,0,7))