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

# Choisir la méthode de calcul
    
    print("\nChoisissez la méthode :")
    print("1. Dichotomie")
    print("2. Balayage")
    
    choix = input("Votre choix : ")

if  choix == "1":
    racine = dichotomie(f, a, b, e)
    print(f"\nMéthode de dichotomie → racine ≈ {racine}")

elif choix == "2":
    racine = balayage(f, a, b, e)
    print(f"\nMéthode du balayage → racine ≈ {racine}")

else:
    print("Choix invalide.")