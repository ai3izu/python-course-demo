def show_balance(balance):
    print(f"Twój stan konta wynosi {balance:.2f} zł")
    
def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Kwota musi być dodatnia")
            else:
                return amount
        except ValueError:
            print("Podaj poprawną wartość numeryczną")
            
def deposit(balance):
    amount = get_amount("Wprowadź kwotę, jaką chcesz wpłacić: ")
    print("Pomyślnie dodano")
    return amount

def withdraw(balance):
    amount = get_amount("Podaj kwotę, którą chcesz wypłacić: ")
    if amount > balance:
        print(f"Podana kwota większa niż balans: {balance:.2f} zł")
        return 0
    else:
        print("Pomyślnie wypłacono pieniądze")
        return amount

def main():
    balance = 0.0
    while True:
        print("============================")
        print("Witaj w banku")
        print("Kliknij 1, aby pokazać balans")
        print("Kliknij 2, aby wpłacić pieniądze")
        print("Kliknij 3, aby wypłacić pieniądze")
        print("Kliknij 4, aby wyjść")
        print("============================")
        
        try:
            user_input = int(input("Wybierz opcję 1-4 -> "))
        except ValueError:
            print("Niepoprawna opcja - wybierz ponownie (1-4)")
            continue
        
        if user_input == 1:
            show_balance(balance)
        elif user_input == 2:
            balance += deposit(balance)
        elif user_input == 3:
            balance -= withdraw(balance)
        elif user_input == 4:
            print("Żegnaj, adios!")
            break
        else:
            print("Niepoprawna opcja - wybierz ponownie (1-4)")
            
if __name__ == "__main__":
    main()