# ''''''
# List comprehension
# Dictionary comprehension
# Set comprehension
# Generator Comprehension
# ''''''

# list_1=[1,2,3,4,53,44,23,52,15,21,18]
# divide_by_3=[]
# for item in list_1:
#     if item%3==0:
#         divide_by_3.append(item)
#
# print(divide_by_3)
#
# print('using list comprehension', [item for item in list_1 if item%3==0 ])

dic1={'a':45,'b':24,'A':90}
print({k.lower():dic1.get(k.lower(),0)+dic1.get(k.upper(),0) for k in dic1.keys()})

gen= (i for i in range(56) if i%3==0)
for item in gen:
    print(item)