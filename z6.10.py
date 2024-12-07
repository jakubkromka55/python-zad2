# Obliczanie wieku psa w psich latach

wiek_czlowieka = int(input("Podaj wiek psa w latach ludzkich: "))

if wiek_czlowieka <= 2:
    wiek_psa = wiek_czlowieka * 10.5
else:
    wiek_psa = 2 * 10.5 + (wiek_czlowieka - 2) * 4

print(f"Wiek psa w latach psich wynosi: {wiek_psa} lat.")
