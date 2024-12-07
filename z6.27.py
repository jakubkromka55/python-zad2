# Program drukujący klawiaturę numeryczną z użyciem pętli while

i = 6  # Zaczynamy od numeru 6
while i >= 0:  # Dopóki i nie jest mniejsze niż 0
    j = 1  # Zaczynamy drukowanie od 1
    while j <= 3:  # Drukujemy 3 liczby w jednym wierszu
        print(f'{i + j}', end=' ')  # Drukujemy liczbę
        j += 1  # Zwiększamy j o 1
    print()  # Przechodzimy do nowego wiersza
    i -= 3  # Zmniejszamy i o 3, aby przejść do następnej kolumny
