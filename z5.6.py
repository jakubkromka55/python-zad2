# Oblicza sumę liczb parzystych od 1 do podanej liczby N za pomocą pętli while

N = 10
sum_even = 0

# Obliczanie sumy liczb parzystych
i = 1
while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1

print(f"Suma liczb parzystych od 1 do {N} wynosi: {sum_even}")
