#1
def bigger(a,b,c):
    max = a

    if b > max:
        max = b
    
    if c > max:
        max = c

    return max

def main():
    A = float(input("Enter 1st float number: "))
    B = float(input("Enter 2st float number: "))
    C = float(input("Enter 1st float number: "))

    print("the max number is ", bigger(A,B,C))


main()

#2
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Before swapping: ",a,b)
a, b = b,a
print("After swapping: ",a,b)


