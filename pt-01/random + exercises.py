import random
range_start = 1
range_stop = 100

rand_number = random.randint(range_start,range_stop)
#random.random() <- 0-1 float 0.12312312123
print(rand_number)

options = ("rock","paper","scissors")
print(random.choice(options))

cards = ["2","3","4","Q","A","K"]
random.shuffle(cards)
print(cards)


#cwiczenia 
# 01 random number
# computer_number = random.randint(1,50)
# guesses = 0
# while True:
#     try:
#         user_number = int(input("podaj liczbe do odgadniecia "))
#         guesses += 1
#         if user_number == computer_number:
#             print(f"Brawo liczba to {computer_number}!")
#             print(f"odgadniecie zajelo {guesses} prob")
#             break
#         elif user_number < computer_number :
#             print("Podaj wieksza liczbe!")
#         else : 
#             print("Podaj mniejsza liczbe!")
#     except ValueError: print("to nie liczba")

# # 01 kamien papier
# options = ("kamien","papier","nozyce")
# player = input("podaj kamien papier lub nozyce ")
# computer = random.choice(options)
# while player not in options:
#     player = input("podaj kamien papier lub nozyce ")

# print(f"Gracz {player} vs Komputer {computer}")
# score = 0
# if player == computer : print("remis")
# elif player == "kamien" and computer == "nozyce" : print("gracz wygral")
# elif player == "papier" and computer == "kamien" : print("gracz wygral")
# elif player == "nozyce" and computer == "papier" : print("gracz wygral")
# else : print("komputer wygral")

#03 dice roller
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("jak duzo kostek? "))
for die in range (num_of_dice):
    dice.append(random.randint(1,6))

print(dice)
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line, end="")
print(len(dice_art))

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()
    
for die in dice:
    total += die
print(f"suma {total}")