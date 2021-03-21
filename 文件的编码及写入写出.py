file1=open(r'C:\Users\15546\OneDrive\桌面\11.txt','r',encoding='utf-8')
a=file1.readlines()
file1.close()#每次打开文件后都要关闭
list1=[]
for i in a:
    i.split()
    b=i.split()
    sum=0
    for c in b[1:]:
        sum+=int(c)
    d=b[0]+str(sum)+'\n'
    list1.append(d)
print(list1)
file2=open(r'C:\Users\15546\OneDrive\桌面\112.txt','w',encoding='utf-8')
q=file2.writelines(list1)#write只能写入字符串，writelines可以写入列表
file2.close()#同样写入后需要关闭

        
        