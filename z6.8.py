# Sprawdzanie, czy obie osoby są dorosłe

# Odczytanie imienia i wieku pierwszej osoby
person1_name = input('Wprowadź imię pierwszej osoby: ')
person1_age = int(input('Wprowadź wiek pierwszej osoby: '))

# Odczytanie imienia i wieku drugiej osoby
person2_name = input('Wprowadź imię drugiej osoby: ')
person2_age = int(input('Wprowadź wiek drugiej osoby: '))

# Sprawdzenie, czy obie osoby mają co najmniej 18 lat
if person1_age >= 18 and person2_age >= 18:
    print(f'Obie osoby: {person1_name} i {person2_name} są dorosłe.')
else:
    print(f'Przynajmniej jedna osoba: {person1_name} lub {person2_name} nie jest dorosła.')
