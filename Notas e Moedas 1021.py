N = float(input())
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
moeda1 = 0
moeda050 = 0
moeda025 = 0
moeda010 = 0
moeda5 = 0
moeda01 = 0
while (N >= 100):
    N-=100
    nota100+=1

if N >= 50:
    N-=50
    nota50+=1

if N >= 20:
    N-=20
    nota20+=1

if N >= 10:
    N-=10
    nota10+=1

if N >= 5:
    N-=5
    nota5+=1

while (N >= 2):
    N-=2
    nota2+=1

if N >= 1:
    N-=1
    moeda1+=1

if N >= 0.50:
    N-=0.50
    moeda050+=1

if N >= 0.25:
    N-=0.25
    moeda025+=1

while (N >= 0.10):
    N-=0.10
    moeda010+=1

if N >=0.05:
    N-=0.05
    moeda5+=1

while (N >= 0.01):
    N-=0.01
    moeda01+=1

print("NOTAS:")
print(nota100,"nota(s) de R$100.00")
print(nota50,"nota(s) de R$50.00")
print(nota20,"nota(s) de R$20.00")
print(nota10,"nota(s) de R$10.00")
print(nota5,"nota(s) de R$5.00")
print(nota2,"nota(s) de R$2.00")
print("MOEDAS:")
print(moeda1,"moeda(s) de R$1.00")
print(moeda050,"moeda(s) de R$0.50")
print(moeda025,"moeda(s) de R$0.25")
print(moeda010,"moeda(s) de R$0.10")
print(moeda5,"moeda(s) de R$0.05")
print(moeda01,"moeda(s) de R$0.01")
