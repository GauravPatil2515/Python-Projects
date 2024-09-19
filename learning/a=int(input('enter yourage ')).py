# a=int(input('enter yourage '))
# print("your age is:",a)

# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# if(a>18):
#     print("you can drive")

# else:
#     ('you cannot drive')

num = int(input("enter the value of number :"))

if(num<0):
    print("NUMBER IS negative")

elif(num > 0 ):
    if(num <=10):
        print("numder is between 1-10")
    elif(num>10 and num<=20):
        print("number is between 11-20")
else:
    print("number is zero") 
