
import random
from math import *

#Partie 1


# 1) ecrire une fonction qui verifie si un nombre est premier :

def premier(n:int):
    d = 2
    while(d <= sqrt(n) ):
        if(n%d == 0):
            return 0 #False --> n N'est pas premier
        d+=1 
    return 1 #True --> n est premier

# Test 1
# test = premier(17)
# print("True --> n est premier" if test == 1 else "False --> n N'est pas premier")



# 2) Écrire une fonction Python qui permet de générer un nombre premier aléatoire supérieur à une borne passée en paramètre.

def gen_preums(b:int):
    nb = random.randint(b + 1, 3 * b)
    while not premier(nb):
        nb += 1
    return nb


#Test 2
# borne = 10
# nombre_premier = gen_preums(borne)
# print(nombre_premier)




# 3) Écrire une fonction qui permet de calculer l'inverse modulaire d'un nombre passé en paramètre. 




def bezout(a,b):
    x = 1
    y = 0
    u = 0
    v = 1
    while b != 0:
        q = a//b 
        r = a%b
        m = x - u*q
        n = y - v*q
        a = b 
        b = r 
        x = u 
        y = v 
        u = m 
        v = n
    return [a,x,y] 


def rec_bezout(a, b):
    if b == 0:
        return [a, 1, 0]
    else:
        q = a // b
        r = a % b
        res = rec_bezout(b, r)
        d = res[0]
        x = res[2]
        y = res[1] - q * res[2]
        return [d, x, y]

def inverse_mod(a,n):
    #verifier si  a est inevrsible 
    if (bezout(a,n)[0] == 1):
        print("inversible")
        return bezout(a,n)[1]
    else:
        print("Element non inversible !")


# Test 3
#print("\n Test Bezout :  ", bezout(5,7))
# print()
# test = inverse_mod(5,7)

# print("l'inverse modulaire est :", test)






#4) Générer deux nombres premiers aléatoires p et q , et stocker la partie n de la clé publique. Fixer une variable globale d contenant l'autre partie de la clé publique.




p = gen_preums(10)
q = gen_preums(10)
print(p ,"," ,q)
n = p * q
φn = (p - 1) * (q - 1)

d = random.randint(1, n)


#global d
# def public_key(b):
#     p = gen_preums(b)
#     q = gen_preums(b)
#     print(p ,"," ,q)
#     n = p * q
#     φn = (p - 1) * (q - 1)
#     d = random.randint(1, n)
#     print("n :", n)
#     print("d :", d)
#     print("φ(n) :", φn)
#     return[n, d, φn]
    

# #Test 4

# print()
print("n :", n)
print("φ(n) :", φn)
# public_key(10)
# e = inverse_mod(d, public_key[2])
# print()
# print(e)



#5) Écrire une fonction chiffrer_rsa qui prend en paramètre un entier n , et qui renvoie la valeur chiffrée à l'aide de la clé (d, n) . On utilisera la fonction de calcul d'exponentiation rapide modulaire vue en cours.



# def expo_rapide(a, k, n):
#     x = a%n
#     if(k == 0):
#         return 1 
#     elif (k%2 == 0 ):
#         aux = expo_rapide(x, k//2, n)
#         res = (aux ** 2)%n
#         return res
#     else: 
#         aux = expo_rapide(x, (k-1)//2, n)
#         res = (x*(aux ** 2)) % n
#         return res

def expo_rapide(a, k, n):
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

def dechiffrer_rsa(cm:int):
    return (cm,φn,d) 