# l = [13,12,156,3,2,7,4,8,4]
# print(l)
# # print(l.reverse)
# # print(l.append(1))
# # l.sort(reverse=True)
# m = l.copy()
# m[0]=0
# print(m)
# m.append(9)

mark = [12,23,34,2,3,24,23 , "hi"]
print(mark)
print(type(mark))
print(mark[0])
print(mark[1])
print(mark[2])
print(mark[7])
print(mark[-3])
print(mark[len(mark)-3])
print(mark[4])
print(mark[5-3])

if 23 in mark:
   print("yes")
else:
   print('NO')


# if 23 in mark:
#    print("yes")
#    print(type(23))
   
# else:
#    print('NO')
   
if"hi" in mark:
   print("yes")
else:
   print("no")



print(mark)
print(mark[1:-1])   
print(mark[1:6])  
print(mark[1:6:3])  
list =[i*i for i in range(4)]
print(list)

list = [i*i for i in range(123) if i%2!=0 ]
print(list)
