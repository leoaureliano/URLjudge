h1,m1,h2,m2 = input().split()
h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)
hora = 0
minutos = 0

if h1 <= h2:
    hora = h2 - h1

else:
    hora = 24 - (h1 - h2)

if m1 != m2:
    minutos =  60 - m1 + m2
    hora-=1
    
    if minutos >= 60:
        hora+=1
        minutos-=60

print("O jogo durou",hora,"HORA(S) E",minutos,"MINUTO(S)")
    
