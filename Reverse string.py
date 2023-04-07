string=input('Enter a word:')
reverse=''

for i in range(len(string)-1,-1,-1):

    reverse=reverse+string[i]
print(reverse)