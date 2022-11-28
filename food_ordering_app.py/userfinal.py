import json

class restaurant:
    def __init__(self):
        self.foods={}
        self.food_id=len(self.foods)+1
        self.user={}
        self.user_id=len(self.user)+1
        self.ordered_items=[]
        self.ordered_items_id=len(self.ordered_items)+1
        
    def add_food_items(self):
        self.name=input("enter the food item name: ")
        self.quantity=input("enter food quantity in (KG): ")
        self.price=int(input("enter food price: "))
        self.discount=int(input("enter discount: "))
        self.stock=int(input("enter stock value: "))
        self.item={"name":self.name,"quantity":self.quantity,"price":self.price,"discount":self.discount,"stock":self.stock}
        self.food_id=len(self.foods)+1
        self.foods[self.food_id]=self.item
        print(self.item)
        print(self.foods)
        with open("food_data.json","w") as f:
            json.dump(self.foods,f)
        print("food item added")
    def remove_food_items(self):
        x=int(input("enter which food id you want to delete"))
        del self.foods[x]
        print("remaining items available in your list: ",self.foods)
        with open("food_data.json","w") as f:
            json.dump(self.foods,f)
        print("**********food item deleted**********")
    def update_food_items(self):
        y=int(input("enter the food id you want to update"))
        del self.foods[y]
        self.name=input("enter the food item name: ")
        self.quantity=input("enter food quantity in (KG): ")
        self.price=int(input("enter food price: "))
        self.discount=int(input("enter discount: "))
        self.stock=int(input("enter stock value: "))
        self.item={"name":self.name,"quantity":self.quantity,"price":self.price,"discount":self.discount,"stock":self.stock}
        self.food_id=len(self.foods)+1
        self.foods[y]=self.item
        print(self.foods)
        with open("food_data.json","w") as f:
            json.dump(self.foods,f)
        print("**********food data updated*********")


    def profile(self):
        self.full_name=input("enter your name")
        self.phone_number=int(input("enter phone number"))
        self.email=str(input("enter your email"))
        self.address=str(input("enter address"))
        self.password=str(input("password"))
        self.user_dict={"name":self.full_name,"number":self.phone_number,"email":self.email,"address":self.address,"password":self.password}
        self.user_id=len(self.user)+1
        self.user[self.user_id]=self.user_dict
        print(self.user_dict)
        print(self.user)
        with open("user_data.json","w") as f:
            json.dump(self.user,f)
        print("user added")
    def login(self):
        print("***********welcome to login page*********")
        while True:
            user_id=input("enter your name")
            password=input("enter your password")
            if user_id==self.full_name and password==self.password:
                print("*********sucessfully loggedin***********")
                
            else:
                print("incorrect details")
            break
    def place_order(self):
        list_of_foods=[{"name":"tandoori chicken","quantity":"4 pieces","price":240},{"name":"vegan burger","quantity":"1 piece","price":320},{"name":"trufle cake","quantity":"500gm","price":900}]
        
        print("******The menu is here********")
        for i in list_of_foods:
            print(f"{list_of_foods.index(i)+1}.{i['name']} [{i['quantity']}] (INR{i['price']})")
        user_input=int(input("enter the food you want to order"))
        if user_input==1:
            
            self.ordered_items.append(list_of_foods[0])
            print(list_of_foods[0])
        elif user_input==2:
            self.ordered_items.append(list_of_foods[1])
            print(list_of_foods[1])
        elif user_input==3:
            self.ordered_items.append(list_of_foods[2])
            print(list_of_foods[2])
        else:
            print("choose valid item")
        with open("self ordered food_data.json","w") as f:
            json.dump(self.ordered_items,f)
        action=int(input("do you want to continue?\n 1 for yes\n 2 for no\n"))
        if action==1:
            print("order placed sucessfully")
        elif action==2:
            print("order cancelled")
        else:
            print("enter valid input")
    def order_history(self):
        for i in self.ordered_items:
            print("previous orders:\n",i)
    def edit_profile(self):
        for i in self.user_dict:
            self.user_dict[i]=input("enter the {i} you want to update:")
            
        print("details updated",self.user_dict)
        with open("user_data.json","w") as f:
            json.dump(self.user,f)
        print("profile updated sucessfully")

r=restaurant()
print("$$$$$$$$$$ WELCOME TO FOOD ORDERING APP $$$$$$$$$$$")
while True:
    role=int(input("enter the role of the app.\n1.admin\n2.user\n0.exit\n"))
    if role==1:
        while True:
            admin_input=int(input("enter your preference: \n1.add food items\n2.edit food items \n3.remove food items\n0.exit\n"))
            if admin_input==1:
                r.add_food_items()
                new_item=int(input("add more items? \n1.yes \n2.no\n"))
                if new_item==1:
                    r.add_food_items()
                elif new_item==2:
                    print("not intrested")
                else:
                    print("choose valid input")
            elif admin_input==2:
                r.update_food_items()
            elif admin_input==3:
                r.remove_food_items()
            elif admin_input==0:
                print("********previous menu*********")
                break
            else:
                print("invalid input, please select from the options")

    elif role==2:
        print("welcome please register yourself")
        r.profile()
        print("login to your account")
        r.login()
        while True:
            options=int(input("select your options from below \n1. for place order\n2.show order history\n3.edit personal details\n0.logout \n"))
            if options==1:
                r.place_order()
                add_orders=int(input("order more\n1.yes\n2.no\n"))
                if add_orders==1:
                    r.place_order()
                elif add_orders==2:
                    print("no")
                else:
                    print("choose valid input")
                    
            elif options==2:
                r.order_history()
            elif options==3:
                r.edit_profile()
            elif options==0:
                break
            print("******previous menu********")
                    
    elif role==0:
        print("THANK YOU")
        break

# programm output:
# $$$$$$$$$$ WELCOME TO FOOD ORDERING APP $$$$$$$$$$$
# enter the role of the app.
# 1.admin
# 2.user
# 0.exit
# 1
# enter your preference: 
# 1.add food items
# 2.edit food items
# 3.remove food items
# 0.exit
# 1
# enter the food item name: dosa
# enter food quantity in (KG): 8
# enter food price: 40
# enter discount: 10
# enter stock value: 10
# {'name': 'dosa', 'quantity': '8', 'price': 40, 'discount': 10, 'stock': 10}
# {1: {'name': 'dosa', 'quantity': '8', 'price': 40, 'discount': 10, 'stock': 10}}
# food item added
# add more items?
# 1.yes
# 2.no
# 1
# enter the food item name: idli
# enter food quantity in (KG): 9
# enter food price: 10
# enter discount: 0
# enter stock value: 30
# {'name': 'idli', 'quantity': '9', 'price': 10, 'discount': 0, 'stock': 30}
# {1: {'name': 'dosa', 'quantity': '8', 'price': 40, 'discount': 10, 'stock': 10}, 2: {'name': 'idli', 'quantity': '9', 'price': 10, 'discount': 0, 'stock': 30}}      
# food item added
# enter your preference:
# 1.add food items
# 2.edit food items
# 3.remove food items
# 0.exit
# 1
# enter the food item name: chicken
# enter food quantity in (KG): 10
# enter food price: 50
# enter discount: 10
# enter stock value: 15
# {'name': 'chicken', 'quantity': '10', 'price': 50, 'discount': 10, 'stock': 15}
# {1: {'name': 'dosa', 'quantity': '8', 'price': 40, 'discount': 10, 'stock': 10}, 2: {'name': 'idli', 'quantity': '9', 'price': 10, 'discount': 0, 'stock': 30}, 3: {'name': 'chicken', 'quantity': '10', 'price': 50, 'discount': 10, 'stock': 15}}
# food item added
# add more items?
# 1.yes
# 2.no
# 2
# not intrested
# enter your preference:
# 1.add food items
# 2.edit food items
# 3.remove food items
# 0.exit
# 2
# enter the food id you want to update3
# enter the food item name: biriyani
# enter food quantity in (KG): 2
# enter food price: 100
# enter discount: 15
# enter stock value: 5
# {1: {'name': 'dosa', 'quantity': '8', 'price': 40, 'discount': 10, 'stock': 10}, 2: {'name': 'idli', 'quantity': '9', 'price': 10, 'discount': 0, 'stock': 30}, 3: {'name': 'biriyani', 'quantity': '2', 'price': 100, 'discount': 15, 'stock': 5}}
# **********food data updated*********
# enter your preference:
# 1.add food items
# 2.edit food items
# 3.remove food items
# 0.exit
# 3
# enter which food id you want to delete3
# remaining items available in your list:  {1: {'name': 'dosa', 'quantity': '8', 'price': 40, 'discount': 10, 'stock': 10}, 2: {'name': 'idli', 'quantity': '9', 'price': 10, 'discount': 0, 'stock': 30}}
# **********food item deleted**********
# enter your preference:
# 1.add food items
# 2.edit food items
# 3.remove food items
# 0.exit
# 0
# ********previous menu*********
# enter the role of the app.
# 1.admin
# 2.user
# 0.exit
# 2
# welcome please register yourself
# enter your namejitu
# enter phone number8763286260
# enter your emailjitu2@gmail.com
# enter addressjoda
# passwordjitu1999
# {'name': 'jitu', 'number': 8763286260, 'email': 'jitu2@gmail.com', 'address': 'joda', 'password': 'jitu1999'}
# {1: {'name': 'jitu', 'number': 8763286260, 'email': 'jitu2@gmail.com', 'address': 'joda', 'password': 'jitu1999'}}
# user added
# login to your account
# ***********welcome to login page*********
# enter your namejitu
# enter your passwordjitu1999
# *********sucessfully loggedin***********
# select your options from below
# 1. for place order
# 2.show order history
# 3.edit personal details
# 0.logout
# 1
# ******The menu is here********
# 1.tandoori chicken [4 pieces] (INR240)
# 2.vegan burger [1 piece] (INR320)
# 3.trufle cake [500gm] (INR900)
# enter the food you want to order1
# {'name': 'tandoori chicken', 'quantity': '4 pieces', 'price': 240}
# do you want to continue?
#  1 for yes
#  2 for no
# 1
# order placed sucessfully
# order more
# 1.yes
# 2.no
# 1
# ******The menu is here********
# 1.tandoori chicken [4 pieces] (INR240)
# 2.vegan burger [1 piece] (INR320)
# 3.trufle cake [500gm] (INR900)
# enter the food you want to order3
# {'name': 'trufle cake', 'quantity': '500gm', 'price': 900}
# do you want to continue?
#  1 for yes
#  2 for no
# 1
# order placed sucessfully
# ******previous menu********
# select your options from below
# 1. for place order
# 2.show order history
# 3.edit personal details
# 0.logout
# 1
# ******The menu is here********
# 1.tandoori chicken [4 pieces] (INR240)
# 2.vegan burger [1 piece] (INR320)
# 3.trufle cake [500gm] (INR900)
# enter the food you want to order2
# {'name': 'vegan burger', 'quantity': '1 piece', 'price': 320}
# do you want to continue?
#  1 for yes
#  2 for no
# 2
# order cancelled
# order more
# 1.yes
# 2.no
# 2
# no
# ******previous menu********
# select your options from below
# 1. for place order
# 2.show order history
# 3.edit personal details
# 0.logout
# 2
# previous orders:
#  {'name': 'tandoori chicken', 'quantity': '4 pieces', 'price': 240}
# previous orders:
#  {'name': 'trufle cake', 'quantity': '500gm', 'price': 900}
# previous orders:
#  {'name': 'vegan burger', 'quantity': '1 piece', 'price': 320}
# ******previous menu********
# select your options from below 
# 1. for place order
# 2.show order history
# 3.edit personal details
# 0.logout
# 3
# enter the {i} you want to update:jiban
# enter the {i} you want to update:9437607860
# enter the {i} you want to update:jiban2@gmail.com
# enter the {i} you want to update:jurudi
# enter the {i} you want to update:jiban1999
# details updated {'name': 'jiban', 'number': '9437607860', 'email': 'jiban2@gmail.com', 'address': 'jurudi', 'password': 'jiban1999'}
# profile updated sucessfully
# ******previous menu********
# select your options from below
# 1. for place order
# 2.show order history
# 3.edit personal details
# 0.logout
# 0
# enter the role of the app.
# 1.admin
# 2.user
# 0.exit
# 0
# THANK YOU


