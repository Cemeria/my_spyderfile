class Book:
    def __init__(self,name,author,word,store=0):
        self.author=author
        self.name=name
        self.recommd=word
        self.store=store
    def __str__(self):
        status='未借出'
        if self.store==1:
            status='以借出'
        return '名称：%s ，作者：%s ，推荐语：%s ，此书%s。'%(self.name,self.author,self.recommd,status)
        # elif 
        
        
class Bookmanger:
    books=[]
    book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
    book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
    book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。',1)
    books.append(book1)
    books.append(book2)
    books.append(book3)
    def mange(self):
            while True:
                choise=int(input('welcome to the bookmanage system,please enter a number to choice'))
                if choise == 1:
                    self.find_all_book()
            
                elif choise == 2:
                    self.add_book()
                    
                elif choise == 3:
                    self.borrow_book()
                    
                elif choise == 4:
                    self.return_book()
                    
                elif choise == 5:
                    self.find_author()
                    
                else:
                    print('see you next time!')
                    break
                    
    def find_all_book(self):
        for book in self.books:
            print(book)
            
    def add_book(self):
        while True:
            author=input('please input the author.')
            name=input('please input the name.')
            word=input('please input the recommded.')
            book=Book(name,author,word)
            self.books.append(book)
            q=input('any other book? ')
            if q=='no':
                break
     
    def check_book(self,check_name):
       
       for book in self.books:
           if book.name == check_name:
               return book
       else:
           return None       
     
    def borrow_book(self):
        check_name=input('please input the book name.')
        q=self.check_book(check_name)
        if q != None:
            if q.store == 0:
                q.store = 1
                print('borrow this book succseeful')
            elif q.store == 1: 
                print('this book is not aviliable now')
        else:
            print('we do not have this book.')
            
    def return_book(self):
        check_name=input('please input the book name.')
        q=self.check_book(check_name)
        if q != None:
            if q.store == 0:
                print('this book is already returned.')
            elif q.store == 1:
                q.store = 0
                print('return book successful.')
        else:
            print('we do not have this book.')
            
    def find_author(self):
        q=input('please input the author.')
        a=[b.author for b in self.books]
        if q in a: 
            print('here is the book.')
            for b in self.books:
                if b.author == q:
                    print(b)
        else:
             print('we dont find the author')
                
g=Bookmanger()
g.mange()



    
