while True:

    factorial = 0
    x = 1
    number =  int(input("Enter a number: "))

    if number == 0:
        print("The factorial of 0 is 1")

    elif number <= -1:
        print("The factorial of negative numbers is not defined.")

    else:
        for i in range (1, number + 1):
            if number > 0:
                x = i * x
            
            factorial = x

        print("The factorial of ", number, "is ", factorial)
        

    print("---------------------------------")


