x,y,z = input().split(" ")
x = float(x)
y = float(y)
z = float(z)

if x >= y + z or y >= x + z or z >= x + y:
    area = ((x + y) * z) / 2
    print("Area =",'{:.1f}'.format(area))
    

else:
    perimetro = x + y + z
    print("Perimetro =",'{:.1f}'.format(perimetro))

