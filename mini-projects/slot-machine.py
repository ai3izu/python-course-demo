import random as rand
import time

SYMBOLS = ['🍒', '🍉', '🔔', '🍋', '⭐']
PAYOUTS = {
    '🍒': 3,
    '🍉': 1.5,
    '🔔': 5,
    '🍋': 0.5,
    '⭐': 10
}

def spin_row():
    return [rand.choice(SYMBOLS) for _ in range(3)]

def display_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")
    
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        return bet * PAYOUTS.get(row[0], 0)
    return 0

def get_valid_bet(userBalance):
    while True:
        bet = input("Podaj wartość swojego zakładu 😋: ")
        if not bet.isdigit():
            print("Podaj wartość numeryczną!!!! 😡")
            continue
        
        bet = int(bet)
        
        if bet > userBalance:
            print(f"Podano za dużą wartość -> stan konta = {userBalance} 😢")
            continue
        
        if bet <= 0:
            print("Zakład musi być większy niż 0 😡!!")
            continue
        
        return bet
    
def main():
    userBalance = 100
    print("***************************")
    print("Witaj we Freaky Casino 😜")
    print("Symbole : 🍒 🍉 🔔 🍋 ⭐")
    print("***************************")  
    
    while True:
        print(f"Twój obecny balans -> {userBalance} zł")
        bet = get_valid_bet(userBalance)
        
        userBalance -= bet
        row = spin_row()
        print("Kręcę....")
        time.sleep(3)
        display_row(row)
        
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Wow wygrałeś {payout} zł")
        else:
            print("Ojejku przegrałeś")
        userBalance += payout
        
        play_again = input("Czy chcesz zagrać ponownie? (1 tak, 2 nie) -> ")
        if play_again == "1":
            if userBalance == 0:
                print("Skończyły ci się środki 😢")
                choice = input("Wybierz 1 aby doładować, albo 2 żeby wyjść -> ")
                if choice == "1":
                    amount = int(input("Podaj kwotę do doładowania -> "))
                    userBalance += amount
                else: 
                    print("Dziękujemy, zapraszamy ponownie")
                    break
        elif play_again == "2":
            print("Dziękujemy, zapraszamy ponownie")
            break
        else:
            print("Nieprawidłowy wybór. Wybierz 1 lub 2.")
    
if __name__ == "__main__":
    main()