names=['小王','小张','小李','小孙','小赵','小周']
a=0
for i in names:

    if a == 3:
        break
    
    
    HR=input('很想要这个人吗？ ')
    if HR == '是':
        print('你，'+names[i]+',已经被录取啦！')
        a+=1
        continue
    
    department=input('很想要这个人吗？')
    if department == '是':
        print('你，'+names[i]+',已经被录取啦！')
        a+=1
        continue

    boss=input('很想要这个人吗？ ')
    if boss == '是':
        print('你，'+names[i]+',已经被录取啦！')
        a+=1
        continue

