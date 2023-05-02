
import random
from math import *

#Partie 1


# 1)Fonction qui verifie si un nombre est premier :

def premier(n:int):
    d = 2
    while(d <= sqrt(n) ):
        if(n%d == 0):
            return 0 #False --> n N'est pas premier
        d+=1 
    return 1 #True --> n est premier


# 2) Fonction qui permet de générer un nombre premier aléatoire supérieur à une borne passée en paramètre:

def gen_preums(b:int):
    nb = random.randint(b + 1, 3 * b)
    while not premier(nb):
        nb += 1
    return nb


# 3) Fonction qui permet de calculer l'inverse modulaire d'un nombre passé en paramètre. 

def bezout(a, b):#Petite optimisation de la fonction bezout avec "divmod()" de python qui renvoie le quotient et le reste dirrectement
    x, y, u, v = 1, 0, 0, 1

    while b != 0:
        q, r = divmod(a, b)
        m, n = x - u * q, y - v * q
        a, b, x, y, u, v = b, r, u, v, m, n

    return a, x, y


def inverse_mod(a,n):
    #verifier si  a est inevrsible 
    if (bezout(a,n)[0] == 1):
        #print("inversible")
        return bezout(a,n)[1]
    else:
        print("Element non inversible !")


#4) Générer deux nombres premiers aléatoires p et q , et stocker la partie n de la clé publique. Fixer une variable globale d contenant l'autre partie de la clé publique.

global d,n,p,q

###### Initialisations Aléatoires ###########
# p = gen_preums(10)                        #  
# q = gen_preums(10)                        #
# print(f"p: {p}, q: {q}")                  #
# n = p * q                                 #
# print(f"n : {n}")                         #
# phi_n = (p - 1) * (q - 1)                 #
#print(f"φ(n) : {phi_n}" )                  #
# d = random.randint(1, n)                  #
#############################################






#5) Fonction chiffrer_rsa qui prend en paramètre un entier n , et qui renvoie la valeur chiffrée à l'aide de la clé (d, n):

def expo_rapide(a, k, n):#Version itterative de la foncion  d'eponentiation rapide donnée sur le pdf du cours
    result = 1
    a = a % n

    while k > 0:
        if k % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        k = k // 2

    return result

def chiffrer_rsa(m:int):
    return expo_rapide(m,d,n)


#6) Fonction dechiffrer_rsa qui prend en paramètre un entier m , qui calcule la partie privée de la clé puis qui déchiffre le message m à l'aide de la clé privée.

def dechiffrer_rsa(mc:int):
    e = inverse_mod(d,phi_n) #Calcul de la clé privée 
    return expo_rapide(mc,e,n) 

#7) Le message chiffré  qui correspond à la note 13 (avec d = 3, n= 33) est 19

p = 11                                       
q = 3                                      
n = p * q                                  
phi_n = (p - 1) * (q - 1)                  
d = 3
print(f"Le message chiffré  qui correspond à la note 13 est : {chiffrer_rsa(13)}")


#8) Vériffer que la clé privée de déchiffrement est 7 

print("La clé privée de déchiffrement est bien 7 !" if inverse_mod(3, 20) == 7 else "Il y a une erreur !")


#9) Si S = 9 alors cela correspond à la note : 15
print(f"Le message '9', correspond à la note :  {dechiffrer_rsa(9)}")

#10) La clé privée de déchiffrement en supposant que la clé publique de chiffrement soit (c = 3, n = 55) est : -13

n = 55 #p = 5 , q = 11 , phi_n = 40
print(f"La clé privée de déchiffrement est : {inverse_mod(d, 40)}")
