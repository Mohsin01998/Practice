

file= ('file.txt','r')
f= file.readlines()

newList=[]
for line in f:
    newList.append(line[:-1])
    print(newList)