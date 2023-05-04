
import random


###############################  Partie 1 ######################################
print("###############################  Partie 2 ######################################\n")
#Exercice 01
print("\n### Exercice 01 : ###\n")

# 1)Fonction qui verifie si un nombre est premier :

def premier(n: int):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True #n est premier



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
        return None


#4) Générer deux nombres premiers aléatoires p et q , et stocker la partie n de la clé publique. Fixer une variable globale d contenant l'autre partie de la clé publique.



###### Initialisations Aléatoires ###########
p = gen_preums(10)                          #  
q = gen_preums(10)                          #
print(f"p: {p}, q: {q}")                    #
n = p * q                                   #
print(f"n : {n}")                           #
phi_n = (p - 1) * (q - 1)                   #
print(f"φ(n) : {phi_n}" )                   #
d = random.randint(1, n)                    #
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



###############################  Partie 2 ######################################

print("\n###############################  Partie 2 ######################################")

#Exercice 02
print("\n### Exercice 02 : ###\n")

#1) Fonction chiffrer_aff qui prend en paramètres deux entiers a et b (la clé de chiffrement), et une chaîne de caractère, et qui renvoie le texte dont chaque lettre a été chiffrée individuellement.

alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                "t", "u", "v", "w", "x", "y", "z", ",", "."]

def chiffrer_aff(a,b,m) :
    mc = ""  #message chiffré  
    for i in range (len(m)):
        indice_chiffree = (a* alphabet.index(m[i]) + b)%29
        mc = mc + alphabet[indice_chiffree]        

    return mc


#2) En utilisant la clé (4, 21) , coder la phrase :  "la clef est dans le coffre ".

print(f"Cela donne :{chiffrer_aff(4,21,'la clef est dans le coffre')}")


#3) Fonction dechiffrer_aff qui prend en paramètres deux entiers a et b, et une chaîne caractère, et qui renvoie la chaîne originale, c'est-à-dire le texte qui a permis d'obtenir la chaîne en paramètre après chiffrement.

def dechiffrer_aff(m,a,b) :
    md = "" #message dechiffré   
    inv_a = inverse_mod(a,29)
    for i in range (len(m)):
        md = md + alphabet[(inv_a * (alphabet.index(m[i]) - b))%29]        
    return md


#4) Déchiffrer le message "v.vlukyu,fwtfyooyn.ws" obtenu à partir de la clé (4, 21)

print(f"'v.vlukyu,fwtfyooyn.ws' Donne : {dechiffrer_aff('v.vlukyu,fwtfyooyn.ws',4,21)}")


#Exercice 03
print("\n### Exercice 03 : ###\n")


#1) Fonction qui détermine les fréquences d'apparition des lettres d'un texte passé en paramètre dans une liste.

def frequency(t):
    t = t.lower()
    occ = {}
    alphabet_occ = {char.lower(): 0 for char in alphabet}
    for l in t:
        alphabet_occ[l] += 1
    for lettre, nb_occ in alphabet_occ.items():
        if nb_occ != 0:
            occ[lettre] = nb_occ
    return occ




#2) Fonction qui prend en paramètre une chaîne de caractères puis qui, à partir de la liste des fréquences d'apparition des caractères dans cette chaîne, associe E et ' ' aux deux caractères les plus fréquents. Ceci donne deux possibilités de clé (a1 , b1 ) ,(a2 , b2 ) , afficher les textes déchiffrés à l'aide de ces deux clés.


#Fonction qui trie un dicctionnaire de façon décroissante trouvée sur internet 
def sort_dictionary(dictionary):
    occ_letters = frequency(dictionary)
    sorted_dict = sorted(occ_letters.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict


def find_keys(c): #Dechiffrer
    sorted_l = sort_dictionary(c) 
    
    #Recuperer incide_max et indice_second_max pour les deux cles: 
    
    #Cle une :
    a = alphabet.index(sorted_l[0][0])
    b = alphabet.index(sorted_l[1][0])
    #Cle deux :
    x = alphabet.index(sorted_l[1][0])
    y = alphabet.index(sorted_l[0][0])
    
    #Calcul de a1 et a2
    a = ((a - b) * inverse_mod(5,29)) %29
    x = ((x - y) * inverse_mod(5,29)) %29
    
    #Les deux clés 
    key_1 = (a , b)
    key_2 = (x, y)
    
    return [key_1, key_2]






#3) Déterminer la clé qui a servi à obtenir le message codé

msc = "akdyne .vxnk bijdju.dfodjoujhrajdcjd.jyboigfjudgfidjnhj..jo.dcjdybiqqnjndj.dcjdcjybiqqnjndfo dhjuukxjsdcvo.dajdyvo.jofdojdcvi.dj.njdyvoofdgfjdcjduvodj, jci.jfndj.dcjduvodcju.iok.kinjz"

print(find_keys(msc))


def THE_key(text, k1, k2):
    test_1 = dechiffrer_aff(text, k1[0], k1[1])
    test_2 = dechiffrer_aff(text, k2[0], k2[1])
    
    french_words = set()  # Set to store French words
    
    # Load French word dictionary
    with open('indice.txt', 'r', encoding='utf-8') as file:
        for word in file:
            french_words.add(word.strip().lower())

    words_1 = test_1.split()  # Split text into words
    words_2 = test_2.split()  # Split text into words

    for word in words_1:
        # Clean the word by removing punctuation and converting to lowercase
        cleaned_word = ''.join(c for c in word if c.isalpha()).lower()
        
        # Check if cleaned word is in the French word dictionary
        if cleaned_word in french_words:
            return k1
    
    for word in words_2:
        # Clean the word by removing punctuation and converting to lowercase
        cleaned_word = ''.join(c for c in word if c.isalpha()).lower()
        
        # Check if cleaned word is in the French word dictionary
        if cleaned_word in french_words:
            return k2

    return False

test2 = chiffrer_aff(4,21,'vive la programmation')


print(THE_key(msc,(7,4),(22,10)))
KEY = THE_key(msc,(7,4),(22,10))
print(dechiffrer_aff(msc,KEY[0],KEY[1]))
print(find_keys(test2))
# print(THE_key(test2,find_keys(test2)[0],find_keys(test2)[1]))


def determiner_cle(chaine_charactere):
    alphabet = [" ","a","b","c","d","e","f","g","h","i",
                "j","k","l","m","n","o","p","q","r","s","t","u","v",
                "w","x","y","z",",","."]
    
    list= frequency(chaine_charactere)
    list_decroissant = sorted(list, key=list.get, reverse=True)
    
    #cas 1:
    e_1 = alphabet.index(list_decroissant[0])
    esp_1 = alphabet.index(list_decroissant[1])

    #cas 2:
    e_2 = alphabet.index(list_decroissant[1])
    esp_2 = alphabet.index(list_decroissant[0])

    b1 = esp_1
    b2 = esp_2
    a1 = ((e_1-b1) * inverse_mod(5,29)) %29
    a2 = ((e_2-b2) * inverse_mod(5,29)) %29

    print("a1:", a1, "b1:", b1, dechiffrer_aff(chaine_charactere, a1, b1))
    print("a2:", a2, "b2:", b2, dechiffrer_aff(chaine_charactere, a2, b2))

#3
message = "akdyne.vxnk bijdju.dfodjoujhrajdcjd.jyboigfjudgfid jnhj..jo.dcjdybiqqnjndj.dcjdcjybiqqnjndfodhjuukxjsdcvo.dajdyvo.jofdojdcvi.dj.njdyvoofdgfjdcjduvodj, jci.jfndj.dcjduvodcju.iok.kinjz"

print(determiner_cle(message))

ms = "papa est un prout et maman fait popo il me faut une phrase plus longue donc tonton est un pid qui pue et tata une vielle chossette"
m = chiffrer_aff(12,6,ms)
print(find_keys(m))
print(dechiffrer_aff(m,12,6))



