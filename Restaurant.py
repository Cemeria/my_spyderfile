class Restaurant():
    def __init__(self,name,type):
        self.restaurant_name=name
        self.restaurant_type=type
        self.number_served=0
    def describe(self):
        print('餐馆名字是%s，餐馆类型是%s'%(self.restaurant_name,self.restaurant_type))            
    def open(self):
        print('is open now')         
    def read_number(self):
        print('now ,we have %s people are eating'%(self.number_served))
    def set_number_served(self,d):
        self.number_served=d
    def increment_number_served(self,f):
        self.number_served+=f
  
class Icecreamstand(Restaurant):
    def __init__(self,name,type):
        Restaurant. __init__(self,name,type)
        #super().__init__(name, type)
        self.flavors=['香草','牛奶','巧克力']
        print(self.flavors)
    
    
        
        
        
        
        
class User():
    def __init__(self,a,b,c):
        self.firstname=a
        self.lastname=b
        self.gentle=c
        self.login_attempts=0
        
    def des_user(self):
        print('该顾客名字叫%s %s ，%s士'%(self.firstname,self.lastname,self.gentle))
    def greeet_user(self):
        q='先生'
        if self.gentle=='女':
            q='女士'
        print('您好，%s'%(self.lastname)+q+',欢迎光临！')
        
    def inc(self):
        self.login_attempts+=1
    def reset(self):
        self.login_attempts=0
        
        
class Pr():
    pri=['can add post','can delete post','can ban users']
    def show_pri(self):
        print(self.pri)
        
class Admin(User):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
        self.pri=['can add post','can delete post','can ban users']
        self.pri=Pr()
    

        
qq=Admin('a','s','f')
qq.pri.show_pri()
# qq=Icecreamstand('zhuzhu', '冰淇淋店') 
        
    
# re=User('ross','geller','man')
# print(re.login_attempts)
# re.inc()
# print(re.login_attempts)
# re.inc()
# print(re.login_attempts)
# re.reset()
# print(re.login_attempts)
