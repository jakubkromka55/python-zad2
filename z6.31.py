import random

# Program generujący 20 losowych liczb całkowitych z zakresu od 5 do 10

for _ in range(20):  # Losujemy 20 liczb
    print(random.randint(5, 10), end=" ")  # Drukujemy każdą wylosowaną liczbę