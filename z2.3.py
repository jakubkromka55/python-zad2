# Program obliczający całkowite zużycie paliwa dla danego dystansu i trybu jazdy
#
driving_mode = input('Podaj tryb jazdy (A/M/E): ').strip().upper()  # Pobranie trybu jazdy, usunięcie spacji, zamiana na wielkie litery
distance = int(input('Podaj dystans w km: '))  # Pobranie dystansu

# Ustalanie zużycia paliwa w zależności od trybu jazdy
if driving_mode == 'A':
    fuel_consumption = 7  # Litry na 100 km
elif driving_mode == 'M':
    fuel_consumption = 9  # Litry na 100 km
elif driving_mode == 'E':
    fuel_consumption = 6  # Litry na 100 km
else:
    print('Nieprawidłowy tryb jazdy')
    fuel_consumption = None

# Obliczanie całkowitego zużycia paliwa
if fuel_consumption is not None:
    total_consumption = (fuel_consumption * distance) / 100
    print(f'Całkowite zużycie paliwa na dystansie {distance} km w trybie {driving_mode} wynosi {total_consumption:.2f} litrów')
