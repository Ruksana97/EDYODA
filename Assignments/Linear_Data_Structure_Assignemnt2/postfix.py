class postfix_evaluation:
     def __init__(self):
         self

def postfix_evaluation(x):

    x=x.split()
    n=len(x)
    stack =[]
    for i in range(n):
       if s[i].isdigit():
#append function is equivalent to push
          stack.append(int(s[i]))
       elif s[i]=="+":
           a=stack.pop()
           b=stack.pop()
           stack.append(int(a)+int(b))
       elif s[i]=="*":
           a=stack.pop()

            b=stack.pop()

            stack.append(int(a)*int(b))

        elif s[i]=="/":\
            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)/int(a))

        elif s[i]=="-":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)-int(a))

    return stack.pop()

#space separtor is required , for solving 2 or more digits .

s="10 2 8 * + 3 -"

val=postfix_evaluation(s)

print(val)