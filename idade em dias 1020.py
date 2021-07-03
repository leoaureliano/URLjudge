idade = int(input())
ano = 0
mes = 0
dias = 0
while (idade >=365):
    ano+=1
    idade-=365

while (idade >=30):
    mes+=1
    idade-=30

while (idade >=1):
    dias+=1
    idade-=1

print(ano,"ano(s)")
print(mes,"mes(es)")
print(dias,"dia(s)")
