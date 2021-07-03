valores = input().split(" ")
A, B, C = valores
A = int(A)
B = int(B)
C = int(C)

maior = (int(A)+int(B) +abs(int(A)-int(B)))/2
resultado = (int(maior) + int(C) + abs(int(maior) - int(C)))/2
print(int(resultado),"eh o maior")
