# Program drukujący tabliczkę mnożenia dla dowolnej liczby wprowadzonej przez użytkownika

liczba = int(input("Wprowadź liczbę: "))  # Wczytujemy liczbę od użytkownika

# Pętla, która drukuje wyniki mnożenia od 1 do 10
for i in range(1, 11):
    print(f"{liczba} x {i} = {liczba * i}")  # Drukujemy wynik mnożenia
