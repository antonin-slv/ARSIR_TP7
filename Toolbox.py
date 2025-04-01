import random 
import math

def euclid(a,b):
    # algorithme d'Euclide : calcule le pgcd et les coefficients de Bezout
    if b == 0:
        return (a, 1, 0)
    else:
        (pgcd, u, v) = euclid(b, a % b)
        return (pgcd, v, u - (a // b) * v)


def inv(a,n):
    # renvoie l'inverse de a modulo n, ou une erreur si a n'est pas inversible
    return 0

def sieve(n):
    # calcule la liste des nombres premiers entre 1 et n
    return []

def is_prime(n):
    # teste si n est premier de manière certaine
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def is_prime_fermat(n):
    # test si un nombre correspond au critère de fermat
    # tout ceux pour qui c'est faux ne sont pas premiers
    # pour les autres, il faut tester
    return (exp(2, n - 1, n) == 1)
    
def exp(a,b,n):
    # calcule a^b mod n (en log(n) multiplications)
    p = 1
    while b > 0:
        if b % 2 != 0:
            p = (p * a) % n
        a = (a * a) % n
        b = b // 2
    return p
    
def div(n):
    # renvoie la liste des diviseurs premiers de n
    if n == 1:
        return []
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            k = n//i
            while (k % i == 0):
                k = k//i
            return [i]+div(k)
    return [n]
        
def gen(n):
    # calcule un générateur de (Z/nZ)*
    # On tire un entier au hasard jusqu'à ce que ce soit un générateur
    # Pour tester si g est générateur, on calcule g^((n-1)/d) mod n pour chaque diviseur premier d de n-1. 
    # Si on tombe sur 1, g n'est pas générateur
    cond = True
    divs = div(n-1)
    while cond:
        g = random.randint(1,n-1)
        cond = any([exp(g,(n-1)/d,n) == 1 for d in divs])
    return g