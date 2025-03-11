import random as rand
words = ("apple", "hello","shark","world")
hangman = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

def display_hangman(wrong_guess):
    print("===============")
    for line in hangman[wrong_guess]:
        print(line)
    print("===============")
    
def display_hint(hint):
    print("===============")
    print("Twoja podpowiedz")
    print(" ".join(hint))
    print("===============")
    
def display_answer(answer):
    print(" ".join(answer))
    
def get_guess(guessed_letters):
    while True:
        guess = input("Podaj litere -> ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Nieprawidlowe wejscie!")  
        elif guess in guessed_letters:
            print(f"{guess} jest juz zgadniety, gluptasie! ")
        else : return guess
        
def main():
    while True:
        answer = rand.choice(words)
        hint = ['_'] * len(answer)
        wrong_guess = 0
        guessed_letters = set()
    
        print("Witaj w hangmanie, odganij slowo")
        while True:
            display_hangman(wrong_guess)
            display_hint(hint)
        
            guess = get_guess(guessed_letters)
            guessed_letters.add(guess)
      
            if guess in answer:
                for index in range(len(answer)):
                    if answer[index] == guess:
                        hint[index] = guess
            else: 
                wrong_guess += 1
            
            if "_" not in hint:
                display_hangman(wrong_guess)
                display_answer(answer)
                print("Wygrales")
                break
            elif wrong_guess >= len(hangman) - 1:
                display_hangman(wrong_guess)
                display_answer(answer)
                print("Przegrales")
                break
        play_again = input("Czy chcesz zagrać ponownie? (tak/nie) -> ").lower()
        if play_again != "tak":
            print("Dziękujemy za grę! Do zobaczenia!")
            break

        
if __name__ == "__main__":
    main()