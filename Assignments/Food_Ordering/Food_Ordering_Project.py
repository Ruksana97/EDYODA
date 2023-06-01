from Admin import *
from User import *
import sys

print('Welcome to Food Ordering App')

while True:
    role=int(input('Please select your role for the food ordering app \n1. Admin \n2. User \n3.Exit \n==>'))
    if role==1:
        y=Admin()
        y.admin_login()
        while True:

            print('Press 1 for Add Food Item')
            print('Press 2 for Edit Food Item')
            print('Press 3 for Remove Food Item')
            print('Press 4 for View Food Item')
            print('Press 0 for Exit')
            admin_input = int(input('Enter your Preference:'))

            if admin_input==1:
                y.add_food_item()
            elif admin_input==2:
                y.edit_food_item()
            elif admin_input==3:
                y.remove_Food_item()
            elif admin_input==4:
                y.view_food_item()
            elif admin_input==0:
                sys.exit()
            else:
                print('Enter a valid input')
    elif role==2:
        y=User()
        while True:

            print('Press 1 for User Registration')
            print('Press 2 for Login')
            print('Press 0 for Exit')
            user_input = int(input('Enter your option:'))
            if user_input==1:
                y.Registration()
                print('*'*100)
            elif user_input==2:

                y.Login_to_Application()
                print('*' * 100)

                while True:
                    print('Press 1 for Place an Order')
                    print('Press 2 for Order History')
                    print('Press 3 for Update Profile')
                    print('Press 0 for Exit')
                    user_input=int(input('Enter your option:'))

                    if user_input == 1:
                        y.Place_an_order()
                        print('*' * 100)

                    if user_input == 2:
                        y.Order_History()
                        print('*' * 100)
                    if user_input == 3:
                        y.Update_Profile()
                        print('*' * 100)
                    if user_input == 0:
                        sys.exit()
    elif user_input==0:
                sys.exit()




    elif role==3:
        sys.exit()


