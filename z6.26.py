# Program sprawdzający poprawność kodu PIN

poprawny_pin = "0805"  # Definiujemy poprawny kod PIN
proby = 3  # Użytkownik ma 3 próby

# Pętla, która umożliwia 3 próby wprowadzenia kodu PIN
while proby > 0:
    pin = input("Wprowadź kod PIN: ")  # Wczytujemy kod PIN
    if pin == poprawny_pin:  # Sprawdzamy, czy kod PIN jest poprawny
        print("Kod PIN poprawny!")  # Kod PIN jest poprawny
        break  # Kończymy pętlę
    else:
        proby -= 1  # Zmniejszamy liczbę prób
        if proby > 0:
            print("Nieprawidłowy... Pozostało prób:", proby)  # Informujemy użytkownika o nieprawidłowym PIN-ie
        else:
            print("Niestety, Twoja karta płatnicza została zablokowana.")  # Jeśli użytkownik przekroczy próby, blokujemy kartę
