users=['mohsin','hammad','usama','ashar']

computer=['rasberry pi','android','iphone','sasta phone']

# for i in range(0,len(users)):
#     print('computer used by', users[i], 'is', computer[i]) 


for i  in range (0, len(users)):
    template='computer used by {1} is {0}'
    print(template.format(users[i],computer[i]))