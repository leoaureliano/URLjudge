n1,n2,n3,n4 = input("").split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

a = n1 * 2
b = n2 * 3
c = n3 * 4
d = n4 * 1 

media = (a + b + c + d)/10
print("Media:"'{:.1f}'.format(media))

if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input(""))
    mediana = (media + exame)/2
    print("Nota do exame:"'{:.1f}'.format(exame))
   
    if mediana >= 5.0:
        print("Aluno aprovado.")
        print("Media final:"'{:.1f}'.format(mediana))
    else:
        print("Aluno reprovado")
        print("Media final:"'{:.1f}'.format(mediana))
