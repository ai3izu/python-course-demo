import math
# += -= *= /=
# potegowanie to **  -> **= 
# mod  %

x = 3.14
y = -4
z = 5
#zaokraglenie
print(round(x)) 
#abs
print(abs(y))
#potega
print(pow(z,2))
#maksimum
print(max(x,y,z))
#minimum
print(min(x,y,z))

#biblioteka math
print(math.pi)



#cwiczenia
r = float(input("podaj promien kola "))
print(f"podany promien {r}\obwod kola wynosi {round(2  * math.pi * r,2)}")
print(f"pole kola wynosi {round(math.pi * math.pow(r,2),2)}")

#pitagoras 
a = float(input("podaj a "))
b = float(input("podaj b "))
print(f"c = {math.sqrt(math.pow(a,2) + math.pow(b,2))}")