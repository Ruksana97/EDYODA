def count(string):
    count_upper=0
    count_lower=0

    for i in string:
        if ord(i) >= ord('A') and ord(i) <=ord('Z') :
            count_upper=count_upper+1
        elif ord(i) >= ord('a') and ord(i) <=ord('z') :
            count_lower+=1

    print('The upper count is:',count_upper)
    print('The lower count is:',count_lower)
    return ''

string=input('')
print(count(string))
print(ord(' '))