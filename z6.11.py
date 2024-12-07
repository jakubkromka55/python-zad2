# Program analizujący cenę produktu
# Jeśli cena produktu spadnie o co najmniej 10%, program drukuje rekomendację zakupu

aktualna_cena = float(input("Podaj aktualną cenę produktu: "))
poprzednia_cena = float(input("Podaj poprzednią cenę produktu: "))

obnizenie = ((poprzednia_cena - aktualna_cena) / poprzednia_cena) * 100

if obnizenie >= 10:
    print("Kup produkt!!")
    print(f"Cena produktu obniżona o {obnizenie:.0f}%")
