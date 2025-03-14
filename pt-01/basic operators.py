#or <- tylko jedno prawdziwe zeby bylo true
#and <- wszystko prawdziwe dla true
#not <- odwraca warunek 

temp = 25
is_raining = False

if temp > 35 or temp < 0 or not is_raining:
    print("event is cancelled")
else: print("still scheduled")


#conditional expression to samo co ternary operator czyli skrocony if 

num = 5
print("liczba dodatnia" if num > 0 else "liczba ujemna")
print("liczba parzysta " if num % 2 == 0 else "liczba nieparzysta")

