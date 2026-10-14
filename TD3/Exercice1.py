n = int(input("combien jours à analyser? "))

consommation_totale = 0
consommation_moyenne = 0 
consommation_depassé = 0
consomation_max = 0

for i in range(n):
    c_jour = int(input("consommation?"))
    consommation_totale += c_jour

    if c_jour > 150:
        consommation_depassé += 1

    if c_jour > consomation_max:
        consomation_max = c_jour 

print("consommation totale = ", 
      consommation_totale)
print("consommation moyenne = ", 
      consommation_totale/n)
print("consommation depassé = ", 
      consommation_depassé)

print("consommation max =", 
      consomation_max)
