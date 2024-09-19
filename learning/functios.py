def calculategmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)


a = 12

b = 15
calculategmean(a ,b)


s = 14
c = 13
calculategmean(s , c)


if (a>b):
    print("first number is greater")
else:
    print("second number is greater")

calculategmean(a ,b)

def isgreater(a ,b):
    if (a>b):
     print("first number is greater")
    else:
     print("second number is greater")



a = 12

b = 15
isgreater(a , b)

def time(a , b):
  if(a >=b+5):
      print("ok")
  else:
     print("not ok") 



a = 16
b = 30

time(a,b)

def average(a=1,b=23,c=12):
    print('average is',(  (a+b+c)/3))

average(c=25)

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("average is:" ,sum/len(numbers))
    return sum /len(numbers)



c = average(2, 34, 34, 43)
print(c)





# average(1,3,4, 23,45, 1000)

# def name(**name):
#     print(type(name))
#     print("hello",name["fname"], name["mname"], name["lname"])

# name(mname = "pravin", lname = " patil", fname =" gaurav")