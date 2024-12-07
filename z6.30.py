# Program drukujący kupon loterii

for i in range(1, 8):  # Iterujemy po wierszach (1 do 7)
    for j in range(i, 50, 7):  # W każdym wierszu drukujemy liczby co 7 (np. 1, 8, 15,...)
        print(f"{j:2}", end=" ")  # Drukujemy liczbę, zachowując formatowanie
    print()  # Przechodzimy do nowego wiersza
