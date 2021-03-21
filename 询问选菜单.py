
import time,random
l1=['麻婆豆腐','水煮青椒鱼','红烧肉','鲑鱼汉堡', '铁板鱿鱼','南瓜寿司']
print('让我帮你选菜吧！')
time.sleep(2)
def q():
    while len(l1)>0:

        b=random.choice(l1)

        a=input(b+'这道菜喜欢吗？请回答是或否')
        l1.remove(b)

        if a=='是':
            print('那今晚就吃它了！')
            break
        elif a=='否':
            continue
        else:
            while True:
                print('请正确输入！')
                a=input(b+'这道菜喜欢吗？请回答是或否')
                if a=='是':
                    print('那今晚就吃它了！')
                    return
                elif a=='否':
                    break
    if len(l1)==0:
        print('没有了')
q()
