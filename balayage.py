


#Définition de notre fonction principale
def Balayage():

    
    #Partie où l'utilisateur devra entrer les diverses valeurs qu'utilisera notre fonction principale  
    print("Soit une fonction f définie sur un intervalle [a;b]")
    a = float(input("Entrez la valeur de a : "))
    b = float(input("Entrez la valeur de b : "))
    e = float(input("Entrez la valeur seuil e : "))
    
    
    x = a ;
    y = b ;
    S = x ;



    #Définition de la fonction qui demandera à l'utilisateur d'entrer l'expression de sa fonction
    def donner_fonct():
        f = input("Veuillez entrer votre fonction, en fonction de x ")
        return lambda x: eval(f)


    
    
    f = donner_fonct() #Stackage de la fonction entrée par l'ulisateur dans la variable f 

    print(" \nx = ", x,"\n y = ", y, "\n S = ", S)
    
    print("\n Les valeurs des images sont : \nf(",x,") = ", f(x))  #Affichage des valeurs de f(x) 
    
    if f(x)== 0 :
        S = y
        print(" x = ", x,"\n y = ", y, "\n S = ", S)

    
    while ((abs(y-x) >= e) and ( f(x)*f(y)< 0)): #La boucle "Tantque" avec les différentes conditions
        
        print("f(",x,") *  f(",y,") = ", f(x)*f(y)," et  |y-x| = ",abs(y-x) )
        S = (x+y)/2
        
        if (f(x)*f(S) < 0):
            y = S
            
        else:
            x = S
        print(" x = ", x,"\n y = ", y, "\n S = ", S)


    print("\n\n On a en fin : ")
    print("f(",x,") *  f(",y,") = ", f(x)*f(y)," et  |y-x| = ",abs(y-x) )
    print(" x = ", x,"\n y = ", y, "\n S = ", S)
        
    return print("\n OUFF!! Terminé... \nLa valeur approchée d'une racine de votre fonction à", e ,"près est :", S); # On retourne la valeur de S

print(Balayage()) # Affichage du resultat final retouné par la fonction principale




