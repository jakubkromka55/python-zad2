# Oblicza sumę liczb parzystych w zakresie <1,10>

sum = 0

# Iterujemy po liczbach w zakresie od 1 do 10 (w tym 10)
for i in range(1, 11):
    if i % 2 != 0:  # Sprawdzamy, czy liczba jest nieparzysta
        continue  # Jeżeli liczba jest nieparzysta, przechodzimy do następnej
    sum += i  # Dodajemy liczbę parzystą do sumy

print(f'Sum of even numbers in the range <1,10> is {sum}')
