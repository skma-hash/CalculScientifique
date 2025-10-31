
#Définition de notre fonction principale
def dichotomie(f, a, b, e):

    
    #Partie où l'utilisateur devra entrer les diverses valeurs qu'utilisera notre fonction principale  

    x = a ;
    y = b ;
    i = 0 ;

    
    #Définition de la fonction qui demandera à l'utilisateur d'entrer l'expression de sa fonction
    #Stackage de la fonction entrée par l'ulisateur dans la variable f 

    print(" \nx = ", x,"\n y = ", y, "\n i = ", i)
    while(f(x)*f(x+e) > 0) :
        x = x+e
        s= x+ e/2
        i = i+1
    print("x = ", x+e)
    print("\n s = ", x + e/2)
    print(" \nx = ", x,"\n y = ", y, "\n i = ", i)
    
    print("\n \n  On obtient :")
    print("x = ", x+e)
    print("\n et  s = ", x + e/2)
    print(" \nx = ", x,"\n y = ", y, "\n i = ", i)
    
    return print("\n Calcul Termine !!!... \nUne valeur approchée de la racine  de  notre fonction à", e ,"près est :", s); # On retourne la valeur de S

# Affichage du resultat final retouné par la fonction principale