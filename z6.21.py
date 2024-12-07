# Program rozbija dowolną kwotę na monety 1, 2 i 5 zł, używając jak najmniejszej liczby monet

kwota = int(input("Wpisz kwotę w złotówkach: "))

# Obliczamy liczbę monet 5 zł, dzieląc kwotę przez 5
monety_5 = kwota // 5
# Pozostała kwota po zabraniu monet 5 zł
pozostalo_po_5 = kwota % 5

# Obliczamy liczbę monet 2 zł, dzieląc pozostałą kwotę przez 2
monety_2 = pozostalo_po_5 // 2
# Pozostała kwota po zabraniu monet 2 zł
pozostalo_po_2 = pozostalo_po_5 % 2

# Liczba monet 1 zł to reszta z dzielenia
monety_1 = pozostalo_po_2

# Wyświetlamy wynik
print(f"Kwota {kwota} zł w monetach:")
print(f"monetach 5 zł: {monety_5}")
print(f"monetach 2 zł: {monety_2}")
print(f"monetach 1 zł: {monety_1}")
