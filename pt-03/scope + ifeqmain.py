# scope LEGB 
# Local -> Enclosed -> Global -> Built-in

#funkcja nie widzi innej funkcji 
def fun1():
    a = 1
    print(a)
    
def fun2():
    b = 2
    #print(a) <- daje blad
    print(b)
    
fun1()
fun2()