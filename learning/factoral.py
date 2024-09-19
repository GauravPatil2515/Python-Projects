# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# number = int(input("Enter a number: "))
# result = factorial(number)
# print(f"The factorial of {number} is {result}")


def factorial(number):
    if number ==  0 or number ==1 :
      return 1
    else:
       return number * factorial(number-1) 
    
n = int(input("ENTER THE NUMBER:"))
result = factorial(n)
print(f"factorial of  {n} is {result}" )
       
 

   

   








