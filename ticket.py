class Ticket: 
    sale=100
    def calu(self,man,child,h):
        global sale
        if h=='周末':
            sale=120
        print(sale)#当        
        a=man*sale+child*(sale/2)
        #a=man*self.sale+child*(self.sale/2)
        
        #当加上self时，调用的是100
        #如果要在类的外部调用类属性，我们得先创建一个实例，再用实例名.属性的格式
        #那么如果想在类的内部调用类属性，而实例又还没创建之前，
        #我们就需要有个变量先代替实例接收数据，这个变量就是参数self。
        #相当于加上self是调用Ticket属性，而不是在函数内重新赋值的sale=120
        return a
b=Ticket()
print(b.calu(1, 0, '周'))
            
    
      