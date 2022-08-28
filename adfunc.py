from variable import admin,user
class adminfunc:
    foodlist=[]
    id=1
    
    def additem(self):
     foodid=self.id
     print("FOOD ID: ",foodid)
     self.id+=1
     foodname=input("Enter name of the dish: ")
     quantity=int(input("Enter quantity: "))
     price=int(input("Enter price: "))
     discount=int(input("Enter discount: "))
     stockleft=int(input("Enter stock left: "))
     menu={'FOOD ID':foodid,
                    'DISH NAME':foodname,
                    'QUANTITY':quantity,
                    'PRICE':price,
                    'DISCOUNT':discount,
                    'STOCK LEFT':stockleft}
        
     if menu.keys in menu:
            if not isinstance(menu[menu.key],list):
                menu[menu.key]=[menu[menu.key]]
                menu[menu.key].append(menu.value)
     print(menu)
     self.foodlist.append(menu)  
     print("New item ADDED successfully!")
        
    def viewitem(self):
        print("Your list of food items...")
        for dish in self.foodlist:
            print(self.foodlist)


    def removeitem(self):
            searchid=int(input("Enter the ID: "))
            for items in self.foodlist:
                if items==searchid:
                    self.foodlist.remove(items)
                    print("This item has been removed successfully!")
                    break
                else:
                    print("ID not found!")
    def edititem(self):
        searchid=int(input("Enter the food ID to edit: "))
        for items in self.foodlist:
            if items==searchid:
                foodid=int(input("Enter food id: "))
                foodname=input("Enter name of the dish: ")
                quantity=input("Enter quantity: ")
                price=input("Enter price: ")
                discount=input("Enter discount: ")
                stockleft=input("Enter stock left: ")

                items.set_foodid(foodid)
                items.set_foodname(foodname)
                items.set_quantity(quantity)
                items.set_price(price)
                items.set_discount(discount)
                items.set_stockleft(stockleft)                
                print("Changes UPDATED successfully!")
                break
            else:
                print("ID not found!")
        
class userfunc:
 customers=[]
 orders=[]
 db={}
 def register(self):
    name=input("Enter full name: ")
    mobile=int(input("Enter 10 digit mobile number: "))
    mail=input("Enter your mail ID: ")
    address=input("Enter your address to deliver: ")
    password=input("Create password: ")                
    password1=input("Confirm password: ")
    if password == password1:
        userfunc.db[name]=password
        print("Successfully registered!")
        obj1=user(name,mobile,mail,address,password)
        userfunc.customers.append(obj1)
        print("Choose from the menu to order...")
        userfunc.placeorder(self)
    else:
        print("Passwords doesnt match")
 def login(self):
    userlogin=input("Enter your username to login: ")
    pwd=input("Enter your password: ")
    if userlogin in userfunc.db.keys():
        if userfunc.db[userlogin]==pwd:
            print("Login successfull")
            userfunc.placeorder()
        else:
            print("Wrong password")
    else:
        print("USER NOT FOUND...Please do register to continue")
        userfunc.register(self)

 def orderhistory(self):
        name=input("Enter your username to view history :")
        customers=[i[0] for i in self.foodlist]
        if name in customers:
            for num in self.foodlist:
                if num[0]==name:
                    print(num[1])
        else:
            print("You didnt place any orders yet")

 def updateprofile(self):
        print("<<<<UPDATE PROFILE>>>>")
        namecheck=input("Enter your username :")
        pwdcheck=input("Enter your password :")
        for user in self.customers:
            if user.name==namecheck and user.password==pwdcheck:
                mobile=int(input("Enter new MOBILE NUMBER to update :"))
                mail=input("Enter new  e-MAIL to update :")
                address=input("Enter new ADDRESS to update :")
                password=input("Enter NEW PASSWORD to update :")

                user.set_mobile(mobile)
                user.set_mail(mail)
                user.set_address(address)
                user.set_password(password)
                print("YOUR PROFILE HAS BEEN UPDATED SUCCESSFULLY")
                break
        else:
            print("Invalid username/Wrong password")
            
 def placeorder(self):
    print("<<<<<PLACE YOUR ORDER>>>>>")

    order=input("ENTER FOOD ID")
    order=order.split(',')
    order[:]=[int(i) for i in order]
    print(order)
    idnum=[i for i in adminfunc.foodlist]
    print(idnum)
    if(all(x in idnum for x in order)):
        for i in order:
            for food in adminfunc.foodlist:
                if food.foodid==i and food.Stock==0:
                    print("OUT OF STOCK")
                    break
                elif food.foodid==i and food.Stock>0:
                    print(food)
                    food.Stock-=1
                    print('1.Place the order\n2.Edit the Order\n') 
                    choice=int(input("Enter your response :"))     
                    if choice==1:
                            for user in userfunc.customers:
                                    userfunc.orders.append([userfunc.name,order])
                                    print("YOUR ORDER IS PLACED!")
                                    break
                            else:
                                print("Invalid Credentials")
                    if choice==2:
                            userfunc.placeorder()
        else:
            print('ID entered not in foodlist')        