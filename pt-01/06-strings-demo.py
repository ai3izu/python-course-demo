# #string methods 
name = input("podaj imie ")
phone_number = input("podaj nr tel ")
# dlugosc stringa
print(f"dlugosc imienia {len(name)}")
#pierwszy zwracany indeks szukanej frazy
print(name.find("s"))
#ostatni zwracany indeks szukanej frazy
print(name.rfind("s"))
#zwiekszenie pierwszej litery => wszystkich to upper
print(name.capitalize() + " " + name.upper())
#sprawdzenie czy string ma  tylko cyfry
print(name.isdigit())
#sprawdzenie czy string ma  tylko alfabetyczne znaki
print(name.isalpha())
#zliczanie podanej frazy
print(phone_number.count("-"))
#zastapienie danego elemetnu podanym
print(phone_number.replace("-"," "))

#przydatna funkcja do metod help() <- print(help(str))


username = input("podaj nazwe uzytkownika ")
print(f"{username} dobrze zwalidowana nazwa" if len(username) < 12 and not username.isdigit() and username.isalpha() else "zle zwalidowane" )


#indexing <- indeksowanie stringow - dostep do elementow poprzez [start : koniec : krok]

credit_number = "1234-0000-1111-2222"

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
print(credit_number[::-1])


#format specifiers <- flagi formatowania wyjscia

price1 = 3.14123
price2 = -986.23
price3 = 123.23
# x:.xf <- precyzja 3.14 == 3.1
# x:10 <- ilosc spacji
# x:010 <- poprzedzenie zerami albo czymkolwiek
# x:>10 <- justify do prawej < do lewej a ^ to centrowanie
# x:+ <- dodanie znaku + - 
# x:, <- przecinek oddzielenie duzych wartosci przecinkiem
print(f"Price 1 is  {price1:.1f}")
print(f"Price 2 is  {price2}")
print(f"Price 3 is  {price3}")