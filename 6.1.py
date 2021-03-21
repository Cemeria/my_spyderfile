# info1={
#       'first_name':'Jay',
#       'last_name':'chou',
#       'age':'42',
#       'city':'taiwan',
#       }
# info2={
#        'first_name':'Ed',
#       'last_name':'Sheeran',
#       'age':'30',
#       'city':'london',
#       }
# info3={
#        'first_name':'Vice',
#       'last_name':'Tone',
#       'age':'29',
#       'city':'goronirin',
#       }
# people=[info1,info2,info3]
# for info in people:
#     print('My name is '+
#           info['first_name']+' '+
#           info['last_name']+
#           ', i am '+
#           info['age']+
#           ' years old, '+
#           "and i was born in "+
#           info['city'])


# tom={'type':'cat',
#       'color':'grey',
#       }
# jerry={'type':'mouse',
#         'color':'yellow',
#         }
# pets=[tom,jerry]
# for pet in pets:
#     print('I am '+
#           str(pet)+  
#           ', and i am a '+
#           pet['type']+
#           ', my color is '+
#           pet['color']+'.'
#           )
# #在不修改原有字典的情况下，打印出以下内容
# # I am tom, and i am a cat, my color is grey.
# # I am jerry, and i am a mouse, my color is yellow.


# info2={
#         'pwd':['print working direct4ory.','打印当前工作路径'],
#         'ls':['list','当前列表'],
#         'mkdir':['make directory','创建目录'],
#         'touch':['make documents','创建文件'],
#         'curl -L -o':['c web','查看网址代码'],
#         'rm':['remove','移除文件'],
#         'cat':['c document','查看文件'],
#         'cd':['change working directory','改变工作路径'],
#         }
# for i,o in info2.items():
#     print('\n'+i+
#           ' means:'
#           )
#     for q in o:  
#         print('\t'+q)
#         if q == o[0]:
#             print('中文意思是：')
        
# for i in sorted(info2.keys()):
#     print(i)
# list1=['pwd','ls','mkwir','print']
# for i in info2.keys():
#     if i in list1:
#         print('thank you, '+i.title())
#     else:
#         print('hi, '+i.title()+', thanks for investion')
        

cities={'beijing':{'country':'china','population':'2153.6w','GDP':'36102.6亿'},
        'chengdu':{'country':'china','population':'1658.1w','GDP':'177167.7亿'},
        'guangzhou':{'country':'china','population':'1530.6w','GDP':'25019亿'},
        }
for i,o in cities.items():
    print(i,':')
    for q,w in o.items():
        print('\n',q,'is',w
             )









    