def count(string):
    count_upper=0
    count_lower=0

    for i in string:
        if ord(i) >= ord('A') and ord(i) <=ord('Z') :
            count_upper+=1
        elif ord(i) >= ord('a') and ord(i) <=ord('z') :
            count_lower+=1

    print('No of Upper case characters:',count_upper)
    print('No of lower case characters:',count_lower)
    return ''


print(count('The quick Brow Fox'))
