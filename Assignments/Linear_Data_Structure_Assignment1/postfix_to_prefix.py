class Postfix_Conversion:

    def __init__(self):
        self.stack=[]

    def postfix_to_prefix(self,exp):
        operator=["(",")","^","*","/","+","-"]
        for i in exp:
            if i not in operator:
                self.stack.append(i)

            elif i in operator:
                top_value=self.stack.pop()
                secondlast_value=self.stack.pop()
                sub=(f"{i}{secondlast_value}{top_value}")
                self.stack.append(sub)
        return "".join(self.stack)

x=Postfix_Conversion

postfix="ABC*+D+"
x.postfix_to_prefix(postfix)
