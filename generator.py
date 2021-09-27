# # factorial by gen
#
# def factorial(n):
#     sum=1
#     for i in range(1,n,1):
#         sum=sum*i
#         yield sum

# sum=factorial(6)
# for sum in factorial(6):
#     print(sum)
# print(sum.__next__())
# print(sum.__next__())

#  fibonacci series

def fibonacci(nterm):
    n1,n2=0,1
    for i in range(nterm):
        yield n1
        nth=n1+n2
        n1=n2
        n2=nth

for n1 in fibonacci(10):
    print(n1)
    
