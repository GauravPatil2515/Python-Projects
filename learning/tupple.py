# tup = (1, 42,43)
# print(type(tup), tup )

# tuple1 = (1,2,2,3,5,4,6)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple1)
# print(tuple2)
# print(len(tup))

# if 34 in tup:
#     print("yes")
# else:
#     print("no")

# tup2 = tup[1:4]
# print(tup2)

# operator

countries = ("Spain", "Italy", "India", "England", "Germany")
print(countries)
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple1.count(3)
# print('Count of 3 in Tuple1 is:', res)

res = Tuple1.index(2,3,1)
print("fi ocura of 2 is ",res)


