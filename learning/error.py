# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#  for i in range(1,10):
#     print(f"{int(a)}x{i}={int(a)*i}")
# except :
#    print("invalid")

# print("HI")
def fun1():
 try:
  num=int(input("enter:"))
 except ValueError:
  print("value")
  return 1
 except IndexError:
  print("index")
  return 0
 finally:
  print("hi")

x = fun1()
print(x)



a =int(input("enter the number:"))

