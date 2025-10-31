

#On défini notre fonction principale 'Newton'
def Newton(f, u, e):

#Partie pour demander à l'utilisateur d'entrer les valeurs nécessaires     
    S = u;
    print("\nInitialement on a :  u = ",u," et S = ", S)
#On écris maintenant des fonctions pour demander à l'utilisateur d'entrer l'expression de sa fonction
    def Entrer_fonction(): 
        f= input("Entrez votre fonction en fonction de u (exemple: u**2 - 6u + 4):  ")
        return lambda u: eval(f)

# De même, on demande à l'ulisateur d'entrer l'expression de la dérrivée de sa fonction 
    def Entrer_der():
        Der_f = input("Entrez la dérrivée de votre fonction  :  ")
        return lambda u: eval(Der_f)
            
#Ici on affecte les valeurs de la fonction puis celle de sa dérrivée correspondente respectivement à F et Der_F entrées par l'utilisateur
    f = Entrer_fonction()
    Der_f = Entrer_der()
    
            
    if (Der_f(u) != 0 ) :
        S = u - (f(u)/Der_f(u)) # calcul du terme suivant de U
    
    print("\n En suite S = ", S)
    while ( (Der_f(S) != 0) and (abs(S-u) >= E ) ): # La structure tantque pour faire les test sur la dérrivée de f et la velur absolue de (s-u)
        print("Der_f(",S,") = ", Der_f(S), " et |S-u| = ", abs(S-u) )

        u = S
        print("u = ", u)
        print("Calcul de la nouvelle valeur de S")
        S = u - (f(u)/Der_f(u))
        print("la nouvelle valeur de S = ", S,"\n")
        
        
    print(" \nOn a en fin   :  u = ", u, ";   S = ", S, "; avec Der_f(",S,") = ", Der_f(S), "  et  |S-u| = ", abs(S-u))
    
    return print( " \n\n\n                La valeur approchée de votre fonction à ",E," près est : S = ", S); # Retour du résultat final 

# Affichage final
