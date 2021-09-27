d1 = {}
# print(type(d1))

d2={"harry":"Burger","rohan":"fish","hammad":"roti","shubham":{"b":"maggie","l":"roti","d":"chicken"}}
d2["usama"]="bbq"
del d2["usama"]
d2["520"]="kebab"
d2.update({"kiran":"icecream"})
# del d2["kiran"]
d3=d2.copy()
del d3["harry"]
# print(d2)
# print(d2["shubham"]["b"])
print(d2.keys())
print(d2.values())