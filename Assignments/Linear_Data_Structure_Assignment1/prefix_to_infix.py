class prefix_to_infix:
    def __init__(self):
        self.stack=[]

    def prefix_to_infix(self,expression):
        operators=['(',")","^","*","/","+","-"]
        for i in range(len(expression)-1,-1,-1): #to read expression from right to left
            if expression[i] in operators:
                sub=(f'{self.stack.pop()}{expression[i]}{self.stack.pop()}')
                print(sub)
                self.stack.append(sub)

            else:
                self.stack.append(expression[i])
        print("".join(self.stack))




x=prefix_to_infix()
prefix="++A*BCD"
x.prefix_to_infix(prefix)











