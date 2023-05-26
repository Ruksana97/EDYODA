class non_repeated_character:
    def __init__(self):
        pass
    def non_repeated_character(self):
        self.string=input('Enter your string:')

        for i in self.string:
            count=0
            if i in self.string.lower():
                self.string.count(i)
                if self.string.count(i)==1:
                    print(i,"is the first non repeated character in",self.string)
                    break

x=non_repeated_character()
x.non_repeated_character()

