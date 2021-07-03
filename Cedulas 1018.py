N = int(input(""))
print(N)
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0
while (N >= 100):
    N-=100
    nota100+=1
 

if N >= 50:
    N-=50
    nota50+=1


while (N >= 20):
       N-=20
       nota20+=1


if N >= 10:
    N-=10
    nota10+=1
  
if N >= 5:
    N-=5
    nota5+=1

while N >= 2:
    N-=2
    nota2+=1

if N == 1:
    N-=1
    nota1+=1


print(nota100,"nota(s) de R$100,00")
print(nota50,"nota(s) de R$50,00")
print(nota20,"nota(s) de R$20,00")
print(nota10,"nota(s) de R$10,00")
print(nota5,"nota(s) de R$5,00")
print(nota2,"nota(s) de R$2,00")
print(nota1,"nota(s) de R$1,00")

