# def function_1(*args):
#     # print(type(args))
#     if len(args)==3:
#         print("Name of the student is ",args[0], "age is ",args[1], "roll no is ", args[2])
#     else:
#         print("Name of the student is ", args[0], "age is ", args[1])

# lis=["mohsin",23]
# print(type(lis))
# function_1(*lis)
#
#
# def printsmarks(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# printsmarks(**markslist)

def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key,value)

lis=["mohsin",23,678]
markslist={"mohsin":98,"hammad":95,"usama":78,"hamza":68,"asma":78}
master("normal arg",*lis,**markslist)