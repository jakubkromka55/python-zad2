# Oblicza wartości ułamków: 1/2, 1/3, ..., 1/10

for i in range(1, 11):  # Iterujemy po liczbach od 1 do 10
    if i == 1:
        continue  # Pomijamy przypadek 1/1, ponieważ jest to liczbą 1,0
    fraction_value = 1 / i  # Obliczamy wartość ułamka 1/i
    print(f'1/{i} = {fraction_value}')
