import dichotomie as dichotomie 
import balayage as balayage 

def f(x) :
    return x**2 - 2 # On cherche la valeur approchee d'une racine de cette fonction 

def main():
    print("Recherche d'une valeur approchee de la racine")
    a = float(input("Entrez une valeur pour la premiere borne de l'intervalle  a :"))
    b = float(input("Entrez une valeur pour la deuxieme borne de l'intervalle b :"))
    e = float(input("Entrez le seuil :"))

    print(f"Soit une fonction f definie sur un intervalle [{a}, {b} ")

    print("Choix invalide.")