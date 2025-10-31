
#Définition de notre fonction principale
def lagrange():

    
    #Partie où l'utilisateur devra entrer les diverses valeurs qu'utilisera notre fonction principale  
    print("Soit une fonction f définie sur un intervalle [a;b]")
    a = float(input("Entrez la valeur de a : "))
    b = float(input("Entrez la valeur de b : "))
    e = float(input("Entrez la valeur seuil e : "))
    
    
    u = a ;
    t = b ;
    s = u ;

    
    #Définition de la fonction qui demandera à l'utilisateur d'entrer l'expression de sa fonction
    def fct():
        f = input("Veuillez entrer votre fonction, en fonction de x ")
        return lambda x: eval(f)

    f = fct() #Stackage de la fonction entrée par l'ulisateur dans la variable f 

    print(" \nu = ", u,"\n t = ", t, "\n s = ", s)
    if (f(t)== 0) :
        s = t
        print(" \nu = ", u,"\n t = ", t, "\n s = ", s)
    while((f(u)*f(t) < 0) and((abs(u-t) >= e))) :
        s= (u*f(t) - tf(u)) / (f(t)-f(u))
    
    print("\n et  s = ", (u*f(t) - tf(u)) / (f(t)-f(u)))
    print(" \nu = ", u,"\n t = ", t, "\n s = ", s)
    if ((f(s)*f(t)) < 0) :
        u = s
            
    else:
        t = s
        
    print(" \nu = ", u,"\n t = ", t, "\n s = ", s)
    print("\n \n  On obtient :")
    print("s = ",  (u*f(t) - tf(u)) / (f(t)-f(u)))
    
    print(" \nu = ", u,"\n t = ", t, "\n s = ", s)
    
    return print("\n Calcul Termine !!!... \nUne valeur approchée de la racine  de  notre fonction à", e ,"près est :", s); # On retourne la valeur de S

print(lagrange()) # Affichage du resultat final retouné par la fonction principal