#list[] uporzadkowane, edytowalne i mozna duplikaty
# set nieuporzadkowane, niemutowalne ale mozna dodawac/usuwac, brak dupliaktow
# tuple uporzadkowalne i niezmienialne, duplikaty mozna *szybsze

#list
fruits = ["apple", "banana", "strawberry"]
# print(dir(fruits))
print("banana" in fruits)
print(fruits[0:1])
fruits[0] = "orange"
fruits.append("berry")
fruits.remove("banana")
fruits.insert(0,"straw")
fruits.reverse() #fruits.sort()
#fruit.clear()
print(fruits.index("straw"))
print(fruits.count("straw"))
for fruit in fruits:
    print(fruit, end=" ")


#set 
cars = {"peguot","audi","bmw","honda"}
print(cars)
print(len(cars))
print("bmw" in cars)
#nie mozna print(cars[x]) i zmienic wartosci
cars.add("dodge")
cars.add("dodge")
cars.pop()
for car in cars:
    print(car, end=" ")
    
    
tuple
foods = ("pizza","spaghetti","kebab","pasta")
print(foods)
print("pizza" in foods)
print(foods.index("kebab"))
print(foods.count("pasta"))
for food in foods:
    print(food, end=" ")

#cwiczenie shopping card program

foods2 = []
prices = []
total = 0

while True: 
    food2 = input("dodaj jedznie do koszyka (q aby wyjsc) ")
    if food2.lower() == "q":
        break
    else : 
        price = int(input(f"podaj cene {food2} w $ "))
        foods2.append(food2)
        prices.append(prices)
        total += price
print("-----KOSZYK-----")
for food2 in foods2:
    print(food2, end=" ")
print(f"twoje zakupy wynosza {total}$")


#2d lista <- lista w liscie / macierz
# meats = ["chicken", "beef", "turkey"]
# vegetables = ["celery", "carrots", "tomatoes"]
# cats = ["silly", "billy", "jilly"]

# groceries = [meats,vegetables,cats]

groceries = [
    ["chicken", "beef", "turkey"],
    ["celery", "carrots", "tomatoes"],
    ["silly", "billy", "jilly"]
]
print(groceries[0]) # <- meats
print(groceries[1]) # <- vegetables
print(groceries[2]) # <- cats
print(groceries[0][0]) # <- chicken
print()
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
    
# #cwiczenie klawiatura
print()
num_pad = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
    ("*",0,"#")
)
for row in num_pad:
    for item in row:
        print(item, end=" ")
    print()
    
# #cwiczenie quizz
print()

questions = ("Pytanie 1", "Pytanie 2", "Pytanie 3", "Pytanie 4", "Pytanie 5")
options = (
    ("a - 22", "b - 15" , "c - 13" , "d - 8"),
    ("a - siema", "b - odp" , "c - mi" , "d - tu"),
    ("a", "b" , "c" , "d"),
    ("a", "b" , "c" , "d"),
    ("a", "b" , "c" , "d")
)
answers = ("c","d","a","d","b")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    guess = input("zgadnij odp (a,b,c,d) ").lower()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score += 1
        print("poprawne")
    else : print (f"niepoprawne, odpowiedz {answers[questions_num]} jest poprawna")
    questions_num += 1
    
print("wynik testu")
print("poprawne odpowiedzi")
for answer in answers:
    print(answer, end=" ")
print("")
print("odpowiedzi uzytkownika")
for guess in guesses:
    print(guess, end=" ")
print()
print(f"wynik testu {int(score/len(questions) * 100)}%")


#dictonaries slowniki {klucz:wartosc} w parach
capitals = {
    "USA":"Washington D.C", 
    "Poland":"Warszawa",
    "Turkey":"Intanbul"
}
print(capitals.get("USA")) # <- jak nie ma to zwraca none
if capitals.get("Japan"):
    print("ten kraj istnieje")
else: print("tan kraj nie istnieje ")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Berlin"})
capitals.pop("Germany")
#capitals.popitem() <- usuwa ostani
#capitals.clear() <- czysci caly

#dostanie samych kluczy bez wartosci
keys = capitals.keys()
#dostanie samych wartosci bez kluczy
values = capitals.values()

for key in capitals.keys():
    print(key)
print()
for value in capitals.values():
    print(value)
print()
print(capitals)

#items <- mozna wypisac klucz z wartoscia
for key, value in capitals.items():
    print(f"{key} : {value}")
    

#cwiczenie menu jedzenia z cena
print()
menu = {
    "chips":20,
    "pizza":10,
    "popcron":5,
    "nachos":7,
    "soda":2,
    "lemonade":11,
}

cart = []
total_price = 0

for key, value in menu.items():
    print(f"{key:10} -> kosztuje {value:2}$")
print("--------------------------")
while True:
    item = input("kup jedznie (q by wyjsc) ").lower()
    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)

for item in cart:
    total_price += menu.get(item)
    print(item, end=" ")
print("\ncalowity koszt ", total_price)