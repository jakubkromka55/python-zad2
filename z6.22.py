# Program drukuje liczby od 1 do 30 z dodatkowymi słowami zależnymi od podzielności przez 3 i 5

for i in range(1, 31):  # Iterujemy przez liczby od 1 do 30
    if i % 3 == 0 and i % 5 == 0:  # Jeśli liczba jest podzielna przez 3 i 5
        print("BINGO", end=" ")
    elif i % 3 == 0:  # Jeśli liczba jest podzielna tylko przez 3
        print("THREE", end=" ")
    elif i % 5 == 0:  # Jeśli liczba jest podzielna tylko przez 5
        print("FIVE", end=" ")
    else:  # Jeśli liczba nie jest podzielna ani przez 3, ani przez 5
        print(i, end=" ")
