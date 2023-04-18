def count(string):
    count_upper=0
    count_lower=0
    low=[]
    for i in range(ord('a'),ord('z')+1):
         low.append(chr(i))
    upper = []
    for i in range(ord('A'), ord('Z') + 1):
         upper.append(chr(i))

    for i in string:
        if i in low:
            count_lower+=1
        elif i in upper:
            count_upper+=1

    print('No of Upper Case Characters:',count_upper)
    print('No of Lower Case Characters:', count_lower)
    return ''

print(count('The quick Brow Fox'))