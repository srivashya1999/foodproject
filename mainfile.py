from adfunc import adminfunc,userfunc

class adminchoice(adminfunc):
    def execute(self,adchoice):
        if adchoice==1:
            print('<'*10,"ADD Food",'>'*10)
            adminfunc.additem(self)
        if adchoice==2:
            print('<'*10,"VIEW Food",'>'*10)
            adminfunc.viewitem(self)
        if adchoice==3:
            print('<'*10,"REMOVE Food",'>'*10)
            adminfunc.removeitem(self)
        if adchoice==4:
            print('<'*10,"EDIT Food",'>'*10)
            adminfunc.edititem(self)

class userchoice(userfunc):
    def execute(self,uchoice):
        if uchoice=='a':
            print('<'*10,'Register Yourself','>'*10)
            userfunc.register(self)
        if uchoice=='b':
            print('<'*10,'Log in','>'*10)
            userfunc.login(self)
        if uchoice==1:
            print('<'*10,'Place New Order','>'*10)
            userfunc.placeorder(self)
        if uchoice==2:
            print('<'*10,'Update Profile','>'*10)
            userfunc.orderhistory(self)
        if uchoice==3:
            print('<'*10,'Update Profile','>'*10)
            userfunc.updateprofile(self)


            
if __name__=="__main__":
   admin='admin'
   admpwd='123'
   userdata=[]
   adminobj=adminchoice()
   userobj=userchoice()
   while True:
      print("1.Admin Login\n2.User Login\n")
      login=int(input("ADMIN OR USER==>>>Enter your choice: "))
      if login==1:
         name=input("Hi admin!,Enter your name: ")
         pwd=input("Enter admin password: ")
         while name==admin and pwd==admpwd:
            print("\n1.ADD ITEM\n2.VIEW ITEM\n3.REMOVE ITEM\n4.EDIT ITEM\n5.HOME PAGE")
            choose=int(input("Enter your choice: "))
            if choose==5:
               print("HOME PAGE")
               break
            adminobj.execute(choose)
      if login==2:
         print("_______WELCOME USER,________")
         first=int(input("1.NEW TO APP!\n2.LOGIN to Order\nEnter your choice: "))
         if first=='a':
            userobj.execute('a')
         if first=='b':
            userobj.execute('b')
            username=input("Enter your Full Name :")
            password=input("Enter your password :")
            for user in userfunc.customers:
               if user.name==username and user.password==password:
                        print(f'Welcome {name}')
                        break
               else:
                    print("invalid credentials")
                    for user in userfunc.customers:
                     while user.name==name and user.password==password:
                        print('\n1.Place new Order\n2.View Order History\n3.Update Profile\n4.Exit User portal')
                        choose=int(input('Enter your choice :'))
                        if choose==4:
                            print("BACK TO HOME PAGE")
                            break 
                        userobj.execute(userchoice)
     

    

