list1=['qwer','erer','yiyu','asdf']
def e(a,i=0):
    for b in a:
        yield i,b
        i=i+1
print(list(e(list1,1)))
    

    

