import math
import time
#while loop 
name = input("podaj imie ")
while name == "":
    print("podaj jeszcze raz bo nie podales")
    name = input("podaj imie ")
print(f"Czes {name}")

# #cwiczenie do while 

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("podaj wartosc inwestyji "))
    if principle <= 0 :
        print("wartosc nie moze byc rowna albo mniejsza od zero")

while rate <= 0:
    rate = float(input("podaj wartosc oprocentowania "))
    if rate <= 0 :
        print("wartosc nie moze byc rowna albo mniejsza od zero") 

while time <= 0:
    time = int(input("podaj czas "))
    if time <= 0 :
        print("wartosc nie moze byc rowna albo mniejsza od zero")  
total = principle * math.pow((1 + rate / 100), time)
print(f"otrzymana ilosc z lokaty {total:+.2f}")   


#petle for 
credit_crd = "1234-5678-9012-3456"
for x in credit_crd:
    print(x)
    
print("od tylu")   

for x in reversed(range(0,20,5)):
    if x == 5: continue
    print(x)    
    
# #cwiczenia for
# #sleep <- usypia na okrelosny czass
timer = int(input("Enter the time in seconds "))
for x in range(timer,0,-1):
    seconds = x % 60
    minutes = int(x / 60)
    hours = int(x/ 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time")

#zagniezdzone petle
for x in range(3):
    for y in range(1,10):
        print(y, end=" ")
    print(end="\n")

#cwiczenie zagniezdzone petle 
rows = int(input("podaj ilosc wierszy "))
symbol = input("podaj symbol do wyswietlenia ")
for x in range(rows):
    for y in range(rows - x):
        print(" ", end="")
    for y in range(1, 2*x):
        print(symbol, end="")
    print(end="\n")
