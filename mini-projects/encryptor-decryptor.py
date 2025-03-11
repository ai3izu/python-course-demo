import random as rand
import string 
from time import sleep
def generate_key():
    chars = list(string.punctuation + string.digits + string.ascii_letters + " ")
    key = chars.copy()
    rand.shuffle(key)
    return dict(zip(chars,key))

def encrypt_msg(message, key):
    encrypted_message = "" 
    for letter in message:
        if letter in key:
            encrypted_message += key[letter]
        else:
            encrypted_message += letter
    return encrypted_message

def decrypt_msg(encrypted, key):
    reverse_key = {value: key for key, value in key.items()}
    decrypted_message = ""
    for letter in encrypted:
        if letter in reverse_key:
            decrypted_message += reverse_key[letter]
        else : 
            decrypted_message += letter
    return decrypted_message

def main():
    print("Witaj w szyfratorze!\nTrwa ladowanie klucza...")
    key = generate_key()
    sleep(3)
    print("Klucz wygenerowano pomyslnie")
    
    original_message = input("Podaj wiadomosc do zaszyfrowania -> ")
    if not original_message:
        print("Nie moze byc pusta wiadomosc ")
        return

    encrypted_message = encrypt_msg(original_message,key)
    print(f"Wiadomosc zaszyfrowana -> {encrypted_message}")
    
    decrypted_message = decrypt_msg(encrypted_message, key)
    print(f"Waidomosc odszyfrowana -> {decrypted_message}")
    
if __name__ == "__main__":
    main()