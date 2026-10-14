#Exercice
N = 5
factorielle = 1

for n in range(N):
    factorielle = 1
    for i in range(n+1):
        factorielle = factorielle *(i+1)
    print("factorielle de ",n+1 , " "
          ,factorielle)