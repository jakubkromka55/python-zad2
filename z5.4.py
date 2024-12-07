import random

# Wylosowana liczba do odgadnięcia z zakresu od 1 do 100
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Zgadnij liczbę z zakresu od 1 do 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Podaj swoją propozycję: "))

    if user_guess < number_to_guess:
        print("Za mało! Spróbuj ponownie.")
    elif user_guess > number_to_guess:
        print("Za dużo! Spróbuj ponownie.")
    else:
        print("Gratulacje! Odgadłeś poprawną liczbę.")
