# Program konwertujący czas z formatu 24-godzinnego na 12-godzinny

czas_24h = input("Wprowadź godzinę (format 24-godzinny): ")
godzina, minuta = map(int, czas_24h.split(":"))

if godzina >= 12:
    godzina_12h = godzina - 12 if godzina > 12 else godzina
    suffix = "pm"
else:
    godzina_12h = godzina
    suffix = "am"

print(f"Godzina w formacie 12-godzinnym: {godzina_12h}:{minuta:02d}{suffix}")
