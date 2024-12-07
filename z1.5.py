# Test jest zaliczony, gdy liczba poprawnie wykonanych zadań wynosi co najmniej 50%
#
total_tasks = 20  # Łączna liczba zadań na teście
tasks_ok = int(input('Podaj liczbę poprawnie wykonanych zadań: '))  # Pobranie liczby poprawnych odpowiedzi
test_passed = False

# Sprawdzenie, czy liczba poprawnych zadań wynosi co najmniej 50%
if tasks_ok >= 0.5 * total_tasks:
    test_passed = True

# Wyświetlenie wyniku
if test_passed:
    print('Gratulacje! Zaliczyłeś test.')
else:
    print('Niestety, nie zaliczyłeś testu.')
