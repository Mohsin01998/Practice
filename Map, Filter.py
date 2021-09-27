# h1=[1,3,4,5]
# sq=[]
# for item in h1:
#     sq.append(item**2)
# print(sq)
# map
# def square(n):
#     return n**2
#
# h1=[1,3,4,5]
#
# sq=list(map(square,h1))
#
# print(sq)

# Filer

# def greater_than_2(n):
#     if n > 2:
#         return True
#     else:
#         return False
#
#
# h1 = [1, 3, 4, 5,-2,-6,7]
# greater_th_2=list(filter(greater_than_2,h1))
# print(greater_th_2)

# Reduce

from functools import reduce

def sum_num(a,b):
    return a+b

h1=[1,3,4,5]
lil1=reduce(sum_num,h1)
print(lil1)