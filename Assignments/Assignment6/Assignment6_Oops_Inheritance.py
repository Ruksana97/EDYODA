class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color

    def description(self):
        print('The name of the dog is:',self.name)
        print('The age of the dog is:',self.age)

    def get_info(self):
        print('The coat color is:',self.coat_color)

class JackRusselTerrier(Dog):
    def fox_hunting(self):
        print('JackRusselTerrier Dog is known to hunt for fox')
    def highlevel_exercise(self):
        print('JackRusselTerrier requires high level of exercise')

class Bulldog(Dog):
    def indoor_dog(self):
        print('Bulldogs are easily adaptable to indoors')
    def overhanging_skin(self):
        print('Bulldogs have over hanging skin')

x=JackRusselTerrier('Oreo',3,'red')
x.description()
x.get_info()
x.fox_hunting()
x.highlevel_exercise

y=Bulldog('Yahoo',2,'white')
y.description()
y.get_info()
y.indoor_dog()
y.overhanging_skin()