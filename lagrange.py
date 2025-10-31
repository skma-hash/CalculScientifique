
#Définition de notre fonction principale
def lagrange(f, a, b, e):

    x = a ;
    y = b ;
    s = x ;

    


    print(" \nx = ", x,"\n y = ", y, "\n s = ", s) # Affichage des vqleurs entrées par l'utilisateur 
    if (f(y)== 0) :
        s = y
        print(" \nx = ", x,"\n y = ", y, "\n s = ", s) # Si l'imqge de t par f est nulle alors c'est la racine recherché 
    while((f(x) * f(y) < 0) and((abs(x-y) >= e))) :
        s= (x * f(y) - y * f(x)) / (f(y) - f(x))
    
    print("\n et  s = ",(x * f(y) - y * f(x)) / (f(y) - f(x)))
    print(" \nx = ", x,"\n y = ", y, "\n s = ", s)
    if ((f(x)*f(y)) < 0) :
        x = s
            
    else:
        y = s
        
    print(" \nx = ", x,"\n y = ", y, "\n s = ", s)
    print("\n \n  On obtient :")
    print("s = ",  (x * f(y) - y * f(x)) / (f(y) - f(x)))
    
    print(" \nx = ", x,"\n y = ", y, "\n s = ", s)
    
    return print("\n Calcul Termine !!!... \nUne valeur approchée de la racine  de  notre fonction à", e ,"près est :", s); # On retourne la valeur de S

# Affichage du resultat final retouné par la fonction principal