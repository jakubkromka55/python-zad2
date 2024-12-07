# Program drukujący pierwsze 20 liczb ciągu Fibonacciego

a, b = 0, 1  # Pierwsze dwa elementy ciągu Fibonacciego
for _ in range(20):  # Drukujemy 20 elementów ciągu
    print(a, end=" ")  
    a, b = b, a + b  # Przekształcamy a i b do kolejnych elementów ciągu
