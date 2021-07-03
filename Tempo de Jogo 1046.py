hora1,hora2 = input().split(" ")
hora1 = int(hora1)
hora2 = int(hora2)
tempo1 = 24 - (hora1 - hora2)
tempo2 = hora2 - hora1

if hora1 >= hora2:
     
     print("O JOGO DUROU",tempo1,"HORAS(S)")

else:
    
    print("O JOGO DUROU",tempo2,"HORAS(S)")
