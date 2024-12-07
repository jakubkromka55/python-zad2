# Program znajdujący N pierwszych liczb pierwszych

N = int(input("Wprowadź liczbę N: "))  # Wczytujemy liczbę N od użytkownika
liczba = 2  # Pierwsza liczba, którą sprawdzamy
liczby_pierwsze = []  # Lista, w której będą przechowywane liczby pierwsze

# Dopóki nie znajdziemy N liczb pierwszych
while len(liczby_pierwsze) < N:
    # Sprawdzamy, czy liczba jest pierwsza
    if all(liczba % i != 0 for i in range(2, int(liczba**0.5) + 1)):
        liczby_pierwsze.append(liczba)  # Dodajemy liczbę do listy liczb pierwszych
    liczba += 1  # Sprawdzamy następną liczbę

# Wyświetlamy znalezione liczby pierwsze
print("Liczby pierwsze:", " ".join(map(str, liczby_pierwsze)))
