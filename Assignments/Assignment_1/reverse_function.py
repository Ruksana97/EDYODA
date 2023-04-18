def rev(string):
    reverse=''
    for i in range(len(string)-1,-1,-1):
        reverse=reverse+string[i]
    return reverse

string='1234abcd'
print(rev(string))
