# CORRECTION EXERCICE 1
billets10 = 100
billets20 = 50
billets50 = 30

nb_retraits = 0
total_distribue = 0

montant = -1

while montant != 0:

    montant = int(input("Montant du retrait : "))

    if montant == 0:
        break

    if montant < 0 or montant > 500 or montant % 10 != 0:
        print("Montant invalide")
    else:
        reste = montant

        nb50 = 0
        nb20 = 0
        nb10 = 0

        # Recherche des billets de 50 €
        while reste >= 50 and nb50 < billets50:
            reste = reste - 50
            nb50 = nb50 + 1

        # Recherche des billets de 20 €
        while reste >= 20 and nb20 < billets20:
            reste = reste - 20
            nb20 = nb20 + 1

        # Recherche des billets de 10 €
        while reste >= 10 and nb10 < billets10:
            reste = reste - 10
            nb10 = nb10 + 1

        if reste != 0:
            print("Retrait impossible : le distributeur ne possède pas les billets nécessaires.")
        else:
            billets50 = billets50 - nb50
            billets20 = billets20 - nb20
            billets10 = billets10 - nb10

            nb_retraits = nb_retraits + 1
            total_distribue = total_distribue + montant

            print("Retrait accepté.")
            print(nb50, "billet(s) de 50 €")
            print(nb20, "billet(s) de 20 €")
            print(nb10, "billet(s) de 10 €")


print("Nombre de retraits :", nb_retraits)
print("Montant total distribué :", total_distribue, "€")
print("Billets de 50 € restants :", billets50)
print("Billets de 20 € restants :", billets20)
print("Billets de 10 € restants :", billets10)
