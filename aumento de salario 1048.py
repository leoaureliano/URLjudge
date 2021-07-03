salario = float(input())
novo = 0
reajuste = 0
contador = 0

if  salario <= 400.00 and salario > 0:
    novo = salario * 1.15
    reajuste = novo - salario
    contador+=15

elif salario >= 400.01 and salario <= 800.00:
    novo = salario * 1.12
    reajuste = novo - salario
    contador+=12
    
elif salario >= 800.01 and salario <= 1200.01:
    novo = salario * 1.10
    reajuste = novo - salario
    contador+=10

elif salario >= 1200.01 and salario <= 2000.00:
    novo = salario * 1.07
    rajuste = novo - salario
    contador+=7

elif salario > 2000.00:
    novo = salario * 1.04
    rajuste = novo - salario
    contador+=4
    




print("Novo salario:",'{:.2f}'.format(novo))
print("Reajuste ganho:",'{:.2f}'.format(reajuste))
print("Em percentual:",contador,"%")
