x,y,z = input().split(" ")
x = float(x)
y = float(y)
z = float(z)

primeironum = 0
segundonum = 0
terceironum = 0

if primeironum == 0:
    if x >= y and x >= z:
        primeironum = x

        if y >= z:
            segundonum = y
            terceironum = z

        else:
            segundonum = z
            terceironum = y


    elif y >= x and y >= z:
        primeironum = y
        
        if x >= z:
            segundonum = x
            terceironum = z

        else:
            segundonum = z
            terceironum = x
            
        
    elif z >= x and  z >= y:
        primeironum = z
        

        if x >= y:
            segundonum = x
            terceironum = y
          

        else:
            segundonum = y
            terceironum = x
           
