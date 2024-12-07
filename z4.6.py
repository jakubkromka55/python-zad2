# Oblicza sumę liczb całkowitych w zakresie <5,10>

sum = 0

# Zmieniamy zakres na liczby od 5 do 10 (w tym 10)
for i in range(5, 11):
    sum += i  # Używamy operatora +=

print(f'Sum is {sum}')
