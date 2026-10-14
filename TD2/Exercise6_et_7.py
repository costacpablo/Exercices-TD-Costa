#Exercise 6
"""nombre = input("nombre?")
nombre = int(nombre)
if nombre%5 ==0 :
    print("hello")

else: 
    print("Bye")"""

#Exercise 7

n1 = int(input("first number?") )
n2 = int(input("second number?") )
operation = input("operation?") #impossible d'utiliser int() pour ces données
#Il faut spécifier chaque cas 
if operation == "+":
    print(n1 + n2)

elif operation == "*":
    print(n1*n2)

elif operation == "-":
    print(n1-n2)

elif operation == "/":
    print(n1/n2)