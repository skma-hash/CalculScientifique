

#On défini notre fonction principale 'Newton'
def Newton():

#Partie pour demander à l'utilisateur d'entrer les valeurs nécessaires     
    u = float(input("Entrez la valeur initiale de u  :  "))
    E = float(input("Entrez la valeur du seuil de précision :  "))
    S = u;
    print("\nInitialement on a :  u = ",u," et S = ", S)
#On écris maintenant des fonctions pour demander à l'utilisateur d'entrer l'expression de sa fonction
    def Entrer_fonction(): 
        F = input("Entrez votre fonction en fonction de u (exemple: u**2 - 6u + 4):  ")
        return lambda u: eval(F)

# De même, on demande à l'ulisateur d'entrer l'expression de la dérrivée de sa fonction 
    def Entrer_der():
        Der_F = input("Entrez la dérrivée de votre fonction  :  ")
        return lambda u: eval(Der_F)
            
#Ici on affecte les valeurs de la fonction puis celle de sa dérrivée correspondente respectivement à F et Der_F entrées par l'utilisateur
    F = Entrer_fonction()
    Der_F = Entrer_der()
    
            
    if (Der_F(u) != 0 ) :
        S = u - (F(u)/Der_F(u)) # calcul du terme suivant de U
    
    print("\n En suite S = ", S)
    while ( (Der_F(S) != 0) and (abs(S-u) >= E ) ): # La structure tantque pour faire les test sur la dérrivée de f et la velur absolue de (s-u)
        print("Der_F(",S,") = ", Der_F(S), " et |S-u| = ", abs(S-u) )

        u = S
        print("u = ", u)
        print("Calcul de la nouvelle valeur de S")
        S =u - (F(u)/Der_F(u))
        print("la nouvelle valeur de S = ", S,"\n")
        
        
    print(" \nOn a en fin   :  u = ", u, ";   S = ", S, "; avec Der_F(",S,") = ", Der_F(S), "  et  |S-u| = ", abs(S-u))
    
    return print( " \n\n\n                La valeur approchée de votre fonction à ",E," près est : S = ", S); # Retour du résultat final 

print(Newton())# Affichage final
