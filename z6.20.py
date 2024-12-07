# Program konwertujący liczbę dziesiętną na liczbę binarną

liczba_dziesietna = int(input("Wprowadź liczbę dziesiętną: "))
liczba_binarna = bin(liczba_dziesietna)[2:]

print(f"{liczba_dziesietna}(10) = {liczba_binarna}(2)")
