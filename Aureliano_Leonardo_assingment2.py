    #Leonardo Aureliano#
import math 

co = 0

while True:
        if not  co == 0:
            co = 0
        print(" ")
        print("Solve Quadratic Equation")
        a = float(input("Enter a = "))
        b = float(input("Enter b = "))
        c = float(input("Enter c = "))

        print("Result:")

        
        delta = b**2 - 4 * a * c
        r1 = (-b + math.sqrt(delta)) / 2 * a
        r2 = (-b - math.sqrt(delta)) / 2 * a
        x1 = format(r1)
        x2 = format(r2)
       
        if a == 0:
            print("This is not a valid quadratic equation")  
            co += 1

        if delta < 0:
            print("There are no real solutions")
            co +=1

        if r1 == r2:
            x1 == x2
            print("x1 = x2 =",x1)
            co +=1

        if co == 0:
            print("x1 =", x1)
            print("x2 =", x2)
            print(" ")
        print("-------------------------")
        
        



