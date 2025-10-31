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

