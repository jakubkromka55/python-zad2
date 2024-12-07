# Sprawdzanie, czy samochód przekroczył ograniczenie prędkości
#
speed_limit = 140  # Ograniczenie prędkości na autostradzie
car_speed = int(input('Podaj prędkość samochodu (km/h): '))  # Pobranie prędkości od użytkownika

# Sprawdzenie, czy prędkość samochodu przekracza ograniczenie
if car_speed > speed_limit:  
    print(f'Twoja prędkość to {car_speed} km/h')  # Wyświetlenie prędkości samochodu
    print('Uwaga: przekroczyłeś ograniczenie prędkości!!')  # Ostrzeżenie o przekroczeniu
