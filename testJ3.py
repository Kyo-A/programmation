# def calcul_double(a):
#   return a * 2

# nb =int(input("Entrez un nombre "))
# print(calcul_double(nb))

# a = 11
# a = 12

# def afficher_nom1(nom):
#   print("bonjour " + nom)

# afficher_nom1("John")

# def afficher_nom2(nom):
#   return nom

# print(afficher_nom2("John"))

# Les habitants de Zorglub paient l’impôt selon les règles suivantes :

# - les hommes de plus de 20 ans paient l’impôt
# - les femmes paient l’impôt si elles ont entre 18 et 35 ans
# - les autres ne paient pas d’impôt

# Le programme demandera donc l’âge et le sexe du Zorglubien, et se 
# prononcera donc ensuite sur le fait que l’habitant est imposable.

def calcul_imposable(age: int, sexe: str): 
    if age > 20 and sexe == "H":
        print("Imposable")
    elif (age >= 18 and age <= 35) and sexe == "F":
        print("imposable")
    else:
        print("non imposable")


# calcul_imposable(17, "F")

# calcul_imposable(19, "F")

# calcul_imposable(29, "H")

# Le programme calculera la somme de N premiers nombres entiers.

# N est une valeur CHOISIE par l’utilisateur de l’algorithme


def calcul_nombreentiers(number):
   s = 0 
   for i in range (1, number+1):
      s = s + i
   print(s)

n=int(input("Valeur de n"))
calcul_nombreentiers(n)

# Les élections législatives, en Guignolerie Septentrionale, obéissent à la règle suivante :

# lorsque l'un des candidats obtient plus de 50% des suffrages, il est élu dès le premier tour.
# en cas de deuxième tour, peuvent participer uniquement les candidats ayant obtenu au moins 12,5% des voix au premier tour.

# Vous devez écrire un algorithme qui permette la saisie des scores de quatre candidats au premier tour. 
# Cet algorithme traitera ensuite le candidat numéro 1 (et uniquement lui) : il dira s'il est élu, battu, s'il se trouve en ballottage favorable 

# (il participe au second tour en étant arrivé en tête à l'issue du premier tour) ou défavorable (il participe au second tour sans avoir été en tête au premier tour).

score_pret1 = int(input("Entrez le score du pretendant 1"))
score_pret2 = int(input("Entrez le score du pretendant 2"))
score_pret3 = int(input("Entrez le score du pretendant 3"))
score_pret4 = int(input("Entrez le score du pretendant 4"))

if(score_pret1 > 50):
    print("Elu au premier tour")
elif (score_pret2 > 50 or score_pret3 > 50 or score_pret4 > 50 or not score_pret1 >= 12.5):
    print("Battu, éliminé, sorti !!!")
elif (score_pret1 >= score_pret2 or score_pret1 >= score_pret3  or score_pret1 >= score_pret4):
    print("Ballotage favorable")
else:
    print("Ballotage Defavorable")


# Une compagnie d'assurance automobile propose à ses clients quatre familles de tarifs identifiables par une couleur, 
# du moins au plus onéreux : tarifs bleu, vert, orange et rouge. 

# Le tarif dépend de la situation du conducteur :

# - un conducteur de moins de 25 ans et titulaire du permis depuis moins de deux ans, se voit attribuer le tarif rouge, 
# si toutefois il n'a jamais été responsable d'accident. 
# Sinon, la compagnie refuse de l'assurer.

# - un conducteur de moins de 25 ans et titulaire du permis depuis plus de deux ans, ou de plus de 25 ans mais titulaire du permis depuis moins de deux ans a le droit au tarif orange 
# s'il n'a jamais provoqué d'accident, au tarif rouge pour un accident, sinon il est refusé.

# - un conducteur de plus de 25 ans titulaire du permis depuis plus de deux ans bénéficie du tarif vert s'il n'est à l'origine d'aucun accident et du tarif orange pour un accident, 
# du tarif rouge pour deux accidents, et refusé au-delà

# De plus, pour encourager la fidélité des clients acceptés, la compagnie propose un contrat de la couleur immédiatement la plus avantageuse s'il est entré dans la maison depuis plus de cinq ans. 
# Ainsi, s'il satisfait à cette exigence, un client normalement "vert" devient "bleu", un client normalement "orange" devient "vert", et le "rouge" devient orange.

# Ecrire l'algorithme permettant de saisir les données nécessaires (sans contrôle de saisie) et de traiter ce problème. Avant de se lancer à corps perdu dans cet exercice, 
# on pourra réfléchir un peu et s'apercevoir qu'il est plus simple qu'il n'en a l'air (cela s'appelle faire une analyse !)

age = int(input("Entrez l'age"))
annee_permis = int(input("Entrez le nombre d'années de permis"))
accidents = int(input("Entrez le nombre d'accidents"))
annee_assurance = int(input("Entrez le nombre d'années d'assurance:"))

if (not age >= 25 and not annee_permis >= 2):
    if (accidents == 0):
        status = "Rouge"
    else:
        status = "Refusé"
elif ((not age >= 25 and annee_permis >= 2) or (age >= 25 and not annee_permis >= 2)):
    if (accidents == 0):
        status = "Orange"
    elif (accidents == 1):
        status = "Rouge"
    else:
        status = "Refusé"
else:
    if (accidents == 0):
        status = "Vert"
    elif (accidents == 1):
        status = "Orange"
    elif (accidents == 2):
        status = "Rouge"
    else:
        status = "Refusé"

if(annee_assurance >= 5):
     if (status == "Rouge"):
         status = "Orange"
     elif (status == "Orange"):
         status = "Vert"
     elif (status == "Vert"):
         status = "Bleu"

print("Votre situation est ", status)