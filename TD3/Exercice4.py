import random
n_question = int(input("Combien de questions ?"))
c = 0
for i in range(n_question):
    n1 = random.randint(0,10)
    n2 = random.randint(0,n1)
    question = "Combien est " + str(n1)+ "-"+ str(n2) + " ?"
    resultat = int(input(question))
    if resultat == n1 - n2:
        c += 1 
        print("très bien !")
print(c)
