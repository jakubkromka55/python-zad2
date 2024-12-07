# Program naliczający rabat za zakup produktów

ilosc_produktow = int(input("Ilość zakupionych produktów: "))
cena_produktu = float(input("Cena produktu: "))

# Rabat 25% za zakupy powyżej 2 sztuk
if ilosc_produktow > 2:
    rabat = 0.25
else:
    rabat = 0

kwota_do_zaplaty = ilosc_produktow * cena_produktu * (1 - rabat)
print(f"Kwota do zapłaty: {kwota_do_zaplaty:.2f}")
