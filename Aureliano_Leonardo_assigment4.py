#1 Question
#TyoeError Raised when a function or operation is applied to an object of incorrect type.
try:
  Brazil = "Rio"
  num = 4
  print(Brazil + num + Brazil)

except TypeError:
    print("TypeError")


try:
    cities = ["Recife","Salvador","SaoPaulo","Brazilia","Cuiaba","Amazonas"]
    place = int(input("NUmber of the city 1-5: "))

    print("The city is ",cities[place-1]," your number is ",place)

except IndexError:
    print("IndexError")


#2 Question
try:
    x = int(input("Enter x: " ))
    y = 10 / x
    print(y)

except ZeroDivisionError:
    print("Cannot divide by zero")
