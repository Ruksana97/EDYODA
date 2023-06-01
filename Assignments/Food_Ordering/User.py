import json
import sys

class User:
    def __init__(self):
        self.order={}
        self.list1=[]
        self.Menu_Book={}
        self.email=None
        self.password=None
    def Registration(self):
        self.full_name = input("Enter your Full Name: ")
        self.phone_number = int(input('Enter your Mobile Number:'))
        self.email= input('Enter your email_id:')
        self.address = input('Enter your address:')
        self.password = input('Enter your password:')
        self.details = {'FullName': self.full_name, 'PhoneNumber': self.phone_number, 'Emailid': self.email,
                        'Address': self.address, 'Password': self.password}

        print('Your Account has been created Successfully')
        with open('user_details.json','w') as d:
            json.dump(self.details,d)

    def Login_to_Application(self):
        if self.email == None or self.password == None:
            print('User is not registered with the food ordering app. \nPlease complete the registration')
            print("*"*100)
            sys.exit()
        Email_id = input('Enter your registered email_id:')
        Password = input('Enter your password:')
        if Email_id == self.email and Password == self.password:
            print('You are now logged in!')
            print("*"*100)
            self.Menu_Book = {1: "Tandoori Chicken(4 Pieces)[INR 240]", 2: "Vegan Burger(1 piece)[INR 320]",
                              3: "Truffle Cake(500gm)[INR 900]"}
            print('Menu Book:\n',self.Menu_Book)
        else:
            print('Please enter valid details ')

    def Place_an_order(self):

            self.Menu_Book = {1: "Tandoori Chicken(4 Pieces)[INR 240]", 2: "Vegan Burger(1 piece)[INR 320]",
                         3: "Truffle Cake(500gm)[INR 900]"}
            print(self.Menu_Book)

            Preference = list(map(int, input('Enter your preferences:').split(',')))
            print('Your Order:')

            for i in Preference:
                print(self.Menu_Book[i])

                self.list1.append(self.Menu_Book[i])
                # print(self.list1)
            place_the_order=int(input("confirm the order? \n1. Confirm\n2.Cancel\n"))
            if  place_the_order == 1:
                print('Your order is placed')
            elif place_the_order==2:
                sys.exit()

            x = ", ".join(self.list1)
            # print(x)


            order_number = len(self.order) + 1
            self.order[order_number] = x
            # print(self.order)
            with open('Order_History.json', 'w') as s:
                json.dump(self.order,s)
                # print('successfull')
    def Order_History(self):
        s=open('Order_History.json','r')
        Order_History=json.load(s)
        print(Order_History)


    def Update_Profile(self):

        i=1
        for k in self.details:
            print(i,'.',k)
            i=i+1

        Update=int(input('Choose above option to update:'))

        if Update==1:
            new_name=input('Enter new name:')
            self.details[self.full_name]=new_name
            print('Your name has been upadted successfully')
        elif Update==2:
            new_PhoneNumber=int(input('Enter the phone number:'))
            self.details[self.phone_number]=new_PhoneNumber
            print('Your Phone Number has been upadted successfully')
        elif Update==3:
            new_email_id=input('Enter new email id:')
            self.details[self.email]=new_email_id
            print('Your email_id has been upadted successfully')
        elif Update==4:
            new_Address=input('Enter new address:')
            self.details[self.address]=new_Address
            print('Your address has been upadted successfully')
        elif Update==5:
            new_Password=input('Enter new password:')
            self.details[self.password]=new_Password
            print('Your password has been upadted successfully')

        with open('user_details.json','w') as d:
            json.dump(self.details,d)




































