# Program do sprawdzania rozmiarów ubrań
# Nieprawidłowy symbol, jeśli podano inny znak niż S, M, L, XL

size = input('Podaj symbol rozmiaru (S, M, L, XL): ').strip().upper()  # Pobranie symbolu rozmiaru, usunięcie spacji, zamiana na wielkie litery

if size == 'S':
    print('S: Mały rozmiar')
elif size == 'M':
    print('M: Średni rozmiar')
elif size == 'L':
    print('L: Duży rozmiar')
elif size == 'XL':
    print('XL: Bardzo duży rozmiar')
else:
    print('Nieprawidłowy symbol')
