import numpy as np
import Toolbox
import random



LISTE_NBS_PR = Toolbox.get5Mprimes()
    
def RSA_gen_keys() :
    # retroune (pq, e) , ((p-1)(q-1),d)
    #   pq , e      la clef publique
    # p-1 q-1 , d   la clef privée
    nbPrs = len(LISTE_NBS_PR)
    q = LISTE_NBS_PR[random.randint(nbPrs//2,nbPrs-1)]
    p = LISTE_NBS_PR[random.randint(nbPrs//2,nbPrs-1)]
    p1q1 = (q - 1) * (p - 1)
    # la clef pub est :  (e,pq)
    while True :
        e = random.randint(2, p1q1)
        if Toolbox.euclid(e, p1q1)[0] == 1:
            break
        #choix de e aléatoire tel que e premier avec (p - 1) (q - 1)
        
    #clef privée : d tq     ed congru à 1 modulo (p-1)(q-1) 
    d = Toolbox.inv(e,p1q1)
    print("p: {}\nq: {}".format(p,q))
    return (p * q,e), (p1q1,d)

def RSA_encode(e,pq,message) :
    #où e, pq est la clef publique
    return Toolbox.exp(message,e,pq)

def RSA_decode(d,pq,message_crypte) :
    #return math.pow(message_crypte,d)
    return Toolbox.exp(message_crypte,d,pq)


def test() :
    (pub,priv) = RSA_gen_keys()

    message = 9
    for i in range(5) :
        message = 10*message +9

    encrypte = RSA_encode(pub[1],pub[0],message)
    print(" pub : {}".format(pub))
    print("priv : {}".format(priv))
    print("msg:{}".format(message))
    print(encrypte)

    decrypte = RSA_decode(priv[1],pub[0],encrypte)
    print(decrypte)

def text_to_int(text:str) :
    somme = 0
    mult = 1
    for code in text.encode('ascii',"replace",):
        somme += mult * code
        mult *= 0xff
    return somme

def int_to_text(number:int) :
    text = ""
    while number > 0 :
        reste = number % 0xff
        number -= reste
        number //= 0xff
        text =  text + chr(reste)
    return text