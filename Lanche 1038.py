cachorro = 4.00
salada = 4.50
bacon = 5.00
torrada = 2.00
refrigerante = 1.50
conta = 0.00

X = input().split()
x,y = X

if x == "1":
    conta +=4.00
    print(conta)
    
if x == "2":
    conta +=4.50
    print(conta)
    
if x == "3":
    conta +=5.00
    print(conta)

if x == "4":
    conta +=2
    print(conta)

if x == "5":
    conta+=5
    print(conta)
  
print("Total: R$",'{:.2f}'.format(conta*float(y)))
