import json


class Admin:
    def __init__(self):
        self.food={}
        self.food_id=len(self.food)+1
    def add_food_item(self):
        self.name=input('Enter the name of the Food item: ')
        self.quantity=int(input('Enter the quantity of the Food Item:'))
        self.price=int(input('Enter the price of the Food Item:'))
        self.stock=int(input('Enter the stock of the FoodItem:'))
        self.discount=int(input('Enter the discount of the Food Item:'))
        self.item={'name':self.name,'quantity':self.quantity,'Price':self.price,'Stock':self.stock,'Disocunt':self.discount}
        self.food_id = len(self.food) + 1
        self.food[self.food_id] = self.item
        print(self.food)
        with open("food_item.json","w") as f:
            json.dump(self.food,f)


    def remove_Food_item(self):
        for k,l in self.food.items():
            print('Food ID is',k, 'and','Food Item is',l)
        del self.food[int(input('Enter the Food ID to be removed:'))]
        print('food item removed successfully')
        print(self.food)
        with open('food_item.json','w') as f:
            json.dump(self.food,f)
        print("=" * 100)
    def view_food_item(self):
        for k,l in self.food.items():
            print('Food ID is',k,'\nFood Item is',l)

    def edit_food_item(self):
        f_id=int(input("Enter the food_id of the food to be edited:"))
        for i in self.food[f_id]:
            self.food[f_id][i]=input(f'enter the {i} you want to update')
        with open('food_item.json', 'w') as f:
            json.dump(self.food, f)
        print('Food item edited successfully')







