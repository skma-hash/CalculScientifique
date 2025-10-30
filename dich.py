a = float(input("Entrez une valeur pour la premiere borne de l'intervalle  a :"))
b = float(input("Entrez une valeur pour la deuxieme borne de l'intervalle b :"))
e = float(input("Entrez le seuil :"))

print(f"Soit une fonction f definie sur un intervalle [{a}, {b} ")

def f(x) :
    return x**2 - 2 # Donnez une expréssion de votre fonction 

def dich(a, b, e) :

    x = a ;
    y = b ; 
    i = 0 ;
    while(f(x)*f(x+e) > 0) :
        x = x+e
        s= x+ e/2
    return s;