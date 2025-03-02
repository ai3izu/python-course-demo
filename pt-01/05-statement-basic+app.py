#ify 
# age = int(input("enter your age "))
# if age >= 18:
#     print("you can use breakbob card")
# else : print("you're not freaky silly billy")


# response = input("enter (Y/N)")
# if response == "Y":
#     print("numnumunumunum")
# else: print("hungry bob")


#cwiczenia 
# 01 - kalkulator
operator = input("podaj operator (+ - * /) ")
num1 = float(input("podaj liczbe 1 "))
num2 = float(input("podaj liczbe 2 "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '/':
    if num2 == 0:
        print("nie mozna dzilic przez zero")
    else: print(num1/num2)
elif operator == '*':
    print(num1*num2)
else: print("nieobslugiwany operator")


# 02 - konwerter wagi
weigth = float(input("podaj wage "))
unit = input("kilogramy czy funty K/L? : ")
if unit == "K":
    print(round(weigth * 2.205,2))
elif unit == "L":
    print(round(weigth / 2.205,2))
else : print("niepoprawna miara")


#03 - konwerter pogody
temperature_unit = input("celcjusz czy farenhajt? C/F ? : ")
temp = float(input("podaj stopnie temeratury "))
if temperature_unit == "C":
    print(f"celcjusz na farenhajta {(temp * (9/5) + 32)}")
elif temperature_unit == "F":
        print(f"farenhajt na celcjusza {(temp - 32) * 5/9}")
else: print("niepoprawna jednostka pogodowa")