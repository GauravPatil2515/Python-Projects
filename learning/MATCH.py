x = int(input("ENTER THE VALUE OF X: "))

match x:
    case 0:
        print("X IS ZERO")
    case 4:
        print('X IS 4')
    case _ if x!=90:
        print(x,"IS NOT 90")
    case _ if x!=80:
        print(x, " IS NOT 80")
    case _:
        print(x) 
           
