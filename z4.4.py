# Program, który drukuje nazwę uczelni z dodatkowymi spacjami między znakami

university = 'Krakow University of Economics'
university_expanded = ''

# Pętla iterująca po każdym znaku w nazwie uczelni
for char in university:
    university_expanded = university_expanded + char + ' '  # dodajemy znak i spację

# Usuwamy ostatnią zbędną spację na końcu
university_expanded = university_expanded.rstrip()

print(university)          # Oryginalna nazwa uczelni
print(university_expanded) # Nazwa uczelni z dodatkowymi spacjami
