# photocopies = input("entrez un nombre de photocopies : ")
# if int(photocopies) < 10:
#     prix = int(photocopies) * 0.5
# elif int(photocopies) < 20:
#     prix = int(photocopies) * 0.4
# else:
#     prix = int(photocopies) * 0.3
# print("Le prix à payer est : ", prix)

# nbr = input("Entrez un nombre : ")
# i = 0
# print("Les 10 nombres suivants sont : ")
# while i < 10:
#     i = i + 1
#     print(int(nbr) + i)

# nbr = input("Entrez un nombre : ")  
# for x in range(10):
#     print(int(nbr) + x)


# som = 0
# nbr = input("Entrez un nombre : ") 
# print("La somme de ")
# for x in range(1, int(nbr) + 1):
#     som = som + x
#     print(x , " + ")
# print(som)

# Nb = int(input("Entrez un nombre entre 1 et 3"))
# while Nb < 1 or Nb > 3:
#     Nb=int(input("Saisie erronée. Entrez un nombre entre 1 et 3 "))
# print("bravo")

# Nb =int(input("Entrez un nombre entre 10 et 20 "))
# while Nb < 10 or Nb > 20:
#     if Nb < 10:
#         print("Plus grand")
#     if Nb > 20:
#         print("Plus petit")
#     Nb = int(input("Saisie erronée. Entrez un nombre entre 10 et 20"))
# print("bravo")


# som = 0
# i = 1
# while som <= 100:
#    som = som + i
#    i = i + 1
#    print(i , " -> " , som)
# print("La valeur cherchée est N= ", som)

# plusGrand = 0
# for x in range(1, 21):
#     Nb =int(input("Entrez un nombre "))
#     if Nb > plusGrand:
#         plusGrand = Nb
# print("Le nombre le plus grand est : ", plusGrand, "et son index est :", x)

# Nb =int(input("Entrez un nombre "))
# fact = 1
# while(Nb > 1): 
#     fact *= Nb 
#     Nb -= 1
# print("La factorielle du chiffre est : ", fact)

from math import factorial

print ("Factorial is", factorial(6))

print ("Factorial is", factorial(7))

print ("Factorial is", factorial(8))

print ("Factorial is", factorial(9))

print ("Factorial is", factorial(10))

