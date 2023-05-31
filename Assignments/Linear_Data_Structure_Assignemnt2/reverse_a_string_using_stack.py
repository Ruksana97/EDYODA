class reverse_string:
    def __init__(self):
        self.stack = []


   

    def reverse(self,string):
        n = len(string)
        for i in range(0,n):
          self.stack.append(string[i])
        string = ""

        for i in range(0, n, 1):
          string += self.stack.pop()
        return string


x=reverse_string()
string = "India"
String = x.reverse(string)
print("Reversed string is " + String)