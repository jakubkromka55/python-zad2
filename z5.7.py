import time

# Funkcja zamieniająca liczby na ich odpowiedniki słowne
def number_to_words(number):
    words = {
        5: "pięć",
        4: "cztery",
        3: "trzy",
        2: "dwa",
        1: "jeden"
    }
    return words.get(number, str(number))  # Domyślnie zwraca liczbę jako tekst

# Pobranie liczby od użytkownika
countdown = int(input("Podaj liczbę sekund do odliczania: "))

while countdown > 0:
    if countdown <= 5:  # Ostatnie 5 sekund drukowane słownie
        print(number_to_words(countdown))
    else:
        print(countdown)
    countdown -= 1
    time.sleep(1)  # Czekaj 1 sekundę

print("Koniec czasu!")
