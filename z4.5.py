# Program szyfrujący tekst za pomocą szyfru Cezara, przesuwając każdą literę o jedno miejsce w prawo

plain_text =  input('Napisz Zdanie')   #'The early bird catches the worm'
encrypted_text = ''

# Iteracja po każdym znaku w tekście
for char in plain_text:
    # Sprawdzamy, czy znak jest literą
    if char.isalpha():
        # Zapisujemy kod znaku (ord()) i przesuwamy go o 1
        new_char = chr(ord(char) + 1)
    else:
        # Jeżeli znak nie jest literą (np. spacja), dodajemy go bez zmian
        new_char = char
        
    # Dodajemy zaszyfrowany znak do zaszyfrowanego tekstu
    encrypted_text += new_char

# Wypisanie wyników
print("Plain text:", plain_text)
print("Encrypted text:", encrypted_text)
