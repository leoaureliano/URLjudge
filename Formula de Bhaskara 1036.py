import math 
a, b, c = float(input(), split())

try:
    delta = b**2 * b - 4 * a * c
    r1 = (-b + math.sqrt(delta)) / 2 * a
    r2 = (-b - math.sqrt(delta)) / 2 * a

print("R1 = {:.5f}".format(r1))
print("R2 = {:.5f}".format(r2))

except:
    print("Impossivel calcular")
