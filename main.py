from math import *
from dichotomie import dichotomie
from balayage import balayage
from lagrange import lagrange
from Newton import Newton

def fct():
    f = input("Veuillez entrer votre fonction, en fonction de x ")
    return lambda x: eval(f)

f = fct()

def main():
    print("Calcul des valeurs qpprochées ")
    print("Méthode 1 : Dichotomie")
    print("Méthode 2 : Balayage")
    print("Méthode 3 : Lagrange")
    print("Méthode 4 : Newton")

    choix = input("Entrez le nom ou le numéro de la méthode : ").lower().strip()

    a = float(input("Entrez la valeur de la borne a : "))
    b = float(input("Entrez la valeur de la borne b : "))

    if "1" in choix or "dichotomie" in choix:
        e = float(input("Entrez le seuil epsilon : "))
        racine = dichotomie(f, a, b, e)
        print(f"\nRésultat (dichotomie) : ", racine)

    elif "2" in choix or "balayage" in choix:
        e  = float(input("Entrez le seuil : "))
        racine = balayage(f, a, b, e)
        print(f"\nRésultat (balayage) :" , racine)

    elif "3" in choix or "lagrange" in choix:
        e  = float(input("Entrez le seuil : "))
        racine = lagrange(f, a, b, e)
        print(f"\nRésultat (Lagrange) : ", racine)

    elif "4" in choix or "newton" in choix:
        e = float(input("Entrez le seuil : "))
        racine = newton(f, u, e)
        print(f"\nRésultat (Newton) : ", racine)

    else:
        print("❌ Méthode inconnue. Veuillez entrer 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()
