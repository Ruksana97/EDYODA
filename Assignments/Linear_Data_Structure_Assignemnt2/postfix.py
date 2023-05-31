class postfix_evaluation:
     def __init__(self):
         self.stack=[]

     def postfix_evaluation(self,expression):


         for i in range(len(expression)):
            if expression[i].isdigit():

                 self.stack.append(int(expression[i]))
            elif expression[i]=="+":
                 last_element=self.stack.pop()
                 secondlast_element=self.stack.pop()
                 self.stack.append(int(last_element)+int(secondlast_element))
            elif expression[i]=="*":
                 last_element=self.stack.pop()

                 secondlast_element=self.stack.pop()

                 self.stack.append(int(last_element)*int(secondlast_element))

            elif expression[i]=="/":
                 last_element=self.stack.pop()

                 secondlast_element=self.stack.pop()

                 self.stack.append(int(secondlast_element)/int(last_element))

            elif expression[i]=="-":

                 last_element=self.stack.pop()

                 secondlast_element=self.stack.pop()

                 self.stack.append(int(secondlast_element)-int(last_element))

         return self.stack.pop()
expression="512+4*+3-"
y=postfix_evaluation()
print(y.postfix_evaluation(expression))


