# x = 1
# y = 2
# z = 0

# z = x
# x = y
# y = z

# print(x)
# print(y)

# Algorithme AffichageNomComplet
# nom = input("entrez votre nom : ")
# prenom = input("entrez votre prenom : ")
# print("Votre nom complet est " + nom, prenom)

# # Algorithme CalculDouble
# a = input("entrez un nombre : ")
# b = int(a) * 2
# print(b)

# # Algorithme AffichagePrenom
# prenom = input("entrez votre prenom : ")
# print("Bonjour " + prenom)

# Algorithme CalculPrixTTC
# prix_HT = input("entrez le prix hors taxe : ")
# nb_Articles = input("entrez le nombre d'articles : ")
# taux_TVA = input("entrez le taux de TVA : ")
# total_TTC = float(prix_HT) * int(nb_Articles) * (1 + float(taux_TVA) / 100)
# print("le prix toutes taxes est : ",  total_TTC)

# Algorithme AffichagePositif
# nombre = input("entrez un chiffre : ")
# if int(nombre) > 0:
#   print("Ce nombre est positif")
# else :
#   print("Ce nombre est négatif")

# nombre = input("entrez un chiffre : ")
# if int(nombre) % 3 == 0 :
#   print("Ce nombre est disible par 3, resultat " , int(nombre) / 3 )
# else :
#   print("Ce nombre n'est pas divisible par 3, resultat " , int(nombre) / 3)

nombre = input("entrez un chiffre : ")
if int(nombre) > 0:
  print("Ce nombre est positif")
elif int(nombre) == 0:
  print("Ce nombre est null")
else:
  print("Ce nombre est negatif")

