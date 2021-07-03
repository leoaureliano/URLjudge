#Está errado pois a saida tem que ser em uma unica linha

X,Y = input("").split(" ")

X = float(X)
Y = float(Y)
           
if X == 00.0 and Y == 00.0:
    print("Origem")
    
elif X >= 00.00 and Y >= 00.00:
    print("Q1")

elif X <= 00.0 and Y >= 00.0:
    print("Q2")

elif X <= 00.0 and Y <= 00.0:    
    print("Q3")

elif X >= 00.0 and Y <= 00.0:
    print("Q4")


while True:
    if X == 0 and Y == 0:
        break

    elif X == 00.00:
        print("Eixo X")

    elif Y == 00.00:
        print("Eixo Y")
    break





#p = input().split()
#x, y = p

#x = float(x)
#y = float(y)

#if x == 0:
#    if y == 0:
#        print('Origem')
#    if y != 0:
#        print('Eixo Y')
#if y == 0:
#    if x != 0:
#        print('Eixo X')
#if x > 0:
#   if y > 0:
#        print('Q1')
#    if y < 0:
#        print('Q4')
#if x < 0:
#    if y > 0:
#        print('Q2')
#    if y < 0:
#        print('Q3')
