#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

#Exercice 1

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné 
    comme jour, heure, minute, seconde."""
    #Arguments temps = (j, h, m, s)
    secondes_jour = temps[0] * 3600*24
    secondes_h = temps[1]* 3600
    secondes_m = temps[2] * 60
    secondes = temps[3]
    total_secondes = secondes_jour + secondes_h + secondes_m + secondes
    return total_secondes

"""temps = (3,23,1,34)
print(type(temps))
a = tempsEnSeconde(temps)
print(a)
print(tempsEnSeconde(temps))   """

#Exercice 2

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde)
      qui correspond au nombre de seconde passé en argument"""
    #combien d'jour y a-t-il dans x secondes ? 
    jour = seconde // (3600*24)
    secondes_restantes = seconde%(3600*24)

    #combien d'heures y a-t-il dans x secondes ? 
    heures = secondes_restantes // 3600
    secondes_restantes = secondes_restantes%3600


    #combien d'minutes y a-t-il dans x secondes ? 
    minutes = secondes_restantes // 60
    secondes_restantes = secondes_restantes%60

    return (jour, heures, minutes, secondes_restantes)
"""temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
secondes = tempsEnSeconde(temps)
print(secondes)"""


#Exercice 3

def pluriel_ou_non(nombre, mot):
    """
    type(mot) = str
    type(nombre) = int 
    Affiche le pluriel de "mot" si nombre > 1, 
    Affiche "mot" si c'est singulier 
    N'affiche rien si nombre == 0 
    """
    if nombre == 0:
        chaine = ""

    elif nombre == 1:
        chaine = "1 " + mot
    else: 
        chaine = str(nombre) + " " +mot + "s"
    return chaine


def afficheTemps(temps):
    jour = temps[0]
    heure = temps[1]
    minute = temps[2]
    seconde = temps[3]

    j = pluriel_ou_non(jour, "jour")#renvoie la chaine pour exprimer les jours 
    h = pluriel_ou_non(heure, "heure")
    m = pluriel_ou_non(minute, "minute")
    s = pluriel_ou_non(seconde, "seconde")

    print(j + " " + h + " " + m + " " + s  )



#afficheTemps((2,3,14,23))




#Exercice 5
def sommeTemps(temps1,temps2):
    #convertir temps1 et temps2 en seconde
    seconde1 = tempsEnSeconde(temps1)
    seconde2 = tempsEnSeconde(temps2)

    #ajouter les deux temps (temps1 + temps2)
    seconde_total = seconde1 + seconde2

    #convertir le seconde en temps  
    temps_final = secondeEnTemps(seconde_total)
    #print(temps_final)
    return temps_final

a = sommeTemps((2,3,4,25),(5,22,57,1))
#print(a)

#Exercice 6 
def proportionTemps(temps,proportion):
    seconde = tempsEnSeconde(temps)
    proportion = int(seconde* proportion)
    temps_final = secondeEnTemps(proportion)
    return temps_final


a = proportionTemps((2,0,36,0),0.2)
#appeler la fonction en échangeant l'ordre des arguments
#print(a)
