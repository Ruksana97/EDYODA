class string_rotation:
    def __init__(self):
        self.string1=""
        self.string2=""
    def rotation(self):
        self.string1=input('enter your first string:').lower()
        self.string2 = input('enter your second string:').lower()
        if self.string1[::-1]==self.string2:
            print('both strings are rotation to each other')
        else:
            print('Bothe are not in rotation to each other')

x=string_rotation()
x.rotation()

