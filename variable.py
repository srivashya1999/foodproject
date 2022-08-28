class admin:
    def __init__(self,foodid,foodname,quantity,price,discount,stockleft):
        self.foodid=foodid
        self.foodname=foodname
        self.quantity=quantity
        self.price=price
        self.discount=discount
        self.stockleft=stockleft
    def __str__(self):
        return f"FOOD ID:{self.foodid}\nDISH NAME:{self.foodname}\nQUANTITY:{self.quantity}\nPRICE:{self.price}\nDISCOUNT:{self.discount}\nSTOCK LEFT:{self.stockleft}"
    
    def set_foodid(self,foodid):
        self.foodid=foodid
    def get_foodid(self):
        return self.foodid

    def set_foodname(self,foodname):
        self.foodname=foodname
    def get_foodname(self):
        return self.foodname

    def set_quantity(self,quantity):
        self.quantity=quantity
    def get_quantity(self):
        return self.quantity

    def set_price(self,price):
        self.price=price
    def get_price(self):
        return self.price

    def set_discount(self,discount):
        self.discount=discount
    def get_discount(self):
        return self.discount

    def set_stockleft(self,stockleft):
        self.stockleft=stockleft
    def get_stockleft(self):
        return self.stockleft

class user:
    def __init__(self,name,mobile,mail,address,password):
        self.name=name
        self.mobile=mobile
        self.mail=mail
        self.address=address
        self.password=password
    def __str__(self):
        return f"FULL NAME:{self.name}\nMOBILE:{self.mobile}\nEmail ID:{self.mail}\nADDRESS:{self.address}\nPASSWORD:{self.password}"
    
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name

    def set_mobile(self,mobile):
        self.mobile=mobile
    def get_mobile(self):
        return self.mobile

    def set_mail(self,mail):
        self.mail=mail
    def get_mail(self):
        return self.mail

    def set_address(self,address):
        self.address=address
    def get_address(self):
        return self.address

    def set_password(self,password):
        self.password=password
    def get_password(self):
        return self.password