annee = 100

if annee%4 == 0:
    if annee%100 ==0 and annee%400!=0:
        print("n'est pas bissextile")
    else:
        print("bissextile")
else:
    print("n'est pas bissextile")