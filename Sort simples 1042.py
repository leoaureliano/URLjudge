x,y,z = input().split(" ")
x = int(x)
y = int(y)
z = int(z)

primeironum = 0
segundonum = 0
terceironum = 0

if primeironum == 0:
    if x <= y and x <= z:
        primeironum = x
        print(primeironum)

        if y <= z:
            segundonum = y
            terceironum = z
            print(segundonum)
            print(terceironum)

        else:
            segundonum = z
            terceironum = y
            print(segundonum)
            print(terceironum)
       

    elif y <= x and y <= z:
        primeironum = y
        print(primeironum)
        
        if x <= z:
            segundonum = x
            terceironum = z
            print(segundonum)
            print(terceironum)

        else:
            segundonum = z
            terceironum = x
            print(segundonum)
            print(terceironum)

        
        
    elif z <= x and  z <= y:
        primeironum = z
        print(primeironum)

        if x <= y:
            segundonum = x
            terceironum = y
            print(segundonum)
            print(terceironum)

        else:
            segundonum = y
            terceironum = x
            print(segundonum)
            print(terceironum)

        

print()
print(x)
print(y)
print(z)
        

    
