import random
from numpy import identity

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
#alphabet = [" ":0, "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9,"j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19,"t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, ",":27, ".":28]

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


m = "akdyne.vxnk bijdju.dfodjoujhrajdcjd.jyboigfjudgfid jnhj..jo.dcjdybiqqnjndj.dcjdcjybiqqnjndfodhjuukxjsdcvo.dajdyvo.jofdojdcvi.dj.njdyvoofdgfjdcjduvodj, jci.jfndj.dcjduvodcju.iok.kinjz"

print(find_keys(m))
print(dechiffrer_aff(m,7,4))


#4) Chiffrer le message "vive la programmation": 
message = "vive la programmation"
test = chiffrer_aff(16,22,message)
print(find_keys(test))

# Le resultat est [(19, 1), (10, 9)] aucune n'est la bonne cle , par consequant cette technique n'est pas valide pour ce message . 
#La raison serai le fait que le message ne contienne qu'un seul "e", ce qui diminue considerablement le taut de reussite de la fonction ...



###############################  Partie 1 ######################################
print("###############################  Partie 3 ######################################\n")
#Exercice 04
print("\n### Exercice 04 : ###\n")

#1) Écrire en Python des fonctions qui permettent:

#de multiplier deux matrices 2 × 2 entre elles :
def mult_mat2x2(mat1, mat2):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res


#de multiplier une matrice par un vecteur de taille 2 :
def mult_vec2(mat,vec):
    res = [0, 0]
    for i in range(2):
        for j in range(2):
            res[i] += mat[i][j] * vec[j]
    return res 

#de multiplier tous les coeffcients d'une matrice par un nombre x:
def mult_matrice(mat, x):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            res[i][j] = mat[i][j] * x 
    return res

#de faire la somme de deux vecteurs de taille 2 :
def somme_vec(v1,v2):
    res = [0, 0]
    for i in range(2):
        res[i] = v1[i] + v2[i] 
    return res


#2) fonction qui renvoie le texte découpé sous forme d'une liste de listes de deux caractères.


def decouper_texte(txt):
    if len(txt) % 2 != 0:
        txt = ' ' + txt
    tdc = [] #texte decoupe
    i = 0
    while i < len(txt):
        tdc.append([txt[i], txt[i+1]])
        i += 2
    return tdc


#3) Fonction qui regroupe les lettres dans l'autre sens 

def rassembler_texte(tdc):
    txt = ''
    for l in tdc:
        txt += l[0] + l[1]
    return txt


#Foncrion qui donne pour chaque paire de lettres son indice dans l'alphabet sous forme de vecteurs 
def texvecs(txt):
    vecs = []
    for l in txt:
        if len(l) >= 2:
            vecs.append([alphabet.index(l[0]), alphabet.index(l[1])])
    return vecs


def chiffrer_hill(txt, matrice_A, vecteur_B):
    tc = ""
    tdc = decouper_texte(txt)
    for p in tdc:
        # pi = pire indexée 
        pi = texvecs([p])
        #pc = paire chiffrée
        pc = mult_vec2(matrice_A, pi[0]) 
        pc = somme_vec(pc, vecteur_B)
        pc = [indice % 29 for indice in pc] # A * v + B [29]
        pc = [alphabet[indice] for indice in pc] # transforme chaque indice en caractere correspendant de l'laphabet
        tc += rassembler_texte([pc])
        
    return tc





#5) chiffrer "vive les vacance" 
test= "vive les vacances"    
mat = [[5, 7], [1, 15]]
vec = [1, 2]
text_chiffree = chiffrer_hill(test,mat, vec)
print(text_chiffree)




#Exercice 05
print("\n### Exercice 05 : ###\n")



#fonction qui forme la matrice augmentee  
def mat_aug(mat):
    I = identity(len(mat),dtype=int).tolist() #matrice identite 
    concat = mat
    #concaenation de la matrice "mat" avec la matrice identité 
    for i in range(len(mat)):
        concat[i].extend(I[i])
    return concat

def inverse_mat(mat):
    # Calcul du déterminant de la matrice
    det = (mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]) % 29
    print(det)
    inv_det = inverse_mod(det, 29)
    print(inv_det)
    if inv_det is None:
        print("La matrice n'est pas inversible modulo 29!")
        return None
    else:
        inv_mat = [[(mat[1][1] * inv_det) % 29, (-mat[0][1] * inv_det) % 29],
                   [(-mat[1][0] * inv_det) % 29, (mat[0][0] * inv_det) % 29]]
        return inv_mat



def dechiffrer_hill(txt, matrice_A, vecteur_B):
    md = "" #message dechiffré   
    inv_a = inverse_mat(matrice_A)
    print(inv_a)
    tdc = decouper_texte(txt)
    for p in tdc:
        pi = texvecs([p])
        vecteur_B_oppose = [-vecteur_B[i] % 29 for i in range(2)]
        pc = somme_vec(pi[0], vecteur_B_oppose)
        pc = mult_vec2(inv_a, pc)
        pc = [indice % 29 for indice in pc]
        pc = [alphabet[indice] for indice in pc]
        md += rassembler_texte([pc])
    return md


print(dechiffrer_hill( text_chiffree,mat,vec))

