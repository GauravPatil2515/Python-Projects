s = {12,2,2,2,4}
print(s)

info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)

s = {1,23,43,12}
s2 ={12,43,65,33}
print(s.union(s2))

h = {1,2,5,4}
b = {4}
print(s.intersection(s2))
s3 = s.union(s2)
S4 = s.intersection(s2)

print(s3.difference(S4))

print(s.isdisjoint(s2))
print(s3.isdisjoint(S4))
print(h.isdisjoint(b))

print(s.issuperset(s2))
print(h.issuperset(b))