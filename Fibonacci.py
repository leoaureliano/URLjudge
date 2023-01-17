import math 

def Fibonacci(n):
    if n <= 1:
        return n
    
    else:
        return(Fibonacci(n-1) + Fibonacci(n-2))
    
terms = 10

for i in range(terms):
    for i in range(terms):
        print(Fibonacci(i)) 
