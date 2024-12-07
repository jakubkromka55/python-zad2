# Program drukujący wzór z gwiazdkami

# Górna część wzoru (rosnąca liczba gwiazdek)
for i in range(1, 11, 2):  # i rośnie od 1 do 10, co drugi krok
    print("* " * i)  # Drukujemy gwiazdki (wielokrotnie, w zależności od i)

# Dolna część wzoru (malejąca liczba gwiazdek)
for i in range(9, 0, -2):  # i maleje od 9 do 1, co drugi krok
    print("* " * i)  # Drukujemy gwiazdki (wielokrotnie, w zależności od i)
