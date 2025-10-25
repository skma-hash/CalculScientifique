a = float(input("Entrez une valeur pour la premiere borne de l'intervalle  a :"))
b = float(input("Entrez une valeur pour la deuxieme borne de l'intervalle b :"))
e = float(input("Entrez le seuil :"))

print(f"Soit une fonction f definie sur un intervalle [{a}, {b}] ")

def f(x) :
    return x**2 - 2 # Donnez une expréssion de votre fonction 

def bal(a, b, e) :

    x = a ;
    y = b ; 
    s = x ;

    if f(y) == 0 :
        s = y
    while((abs(y-x) >= e) and ( f(x)*f(y) < 0)) :
        s = (x+y)/2
        if f(x)*f(s) < 0 :
            y = s
        else:
            x = s
    return s; 

