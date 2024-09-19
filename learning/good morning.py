time = float(input("enter the time "))

if(time < 12):
  print("good morning")
elif(time > 12 and time < 18):
  print("good afternoon")
elif(time > 18 and time < 24 ):
  print("good night")
else:
  print("you are alien")