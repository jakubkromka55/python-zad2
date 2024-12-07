# Program przeprowadzający ankietę

informatyka = input("Czy interesujesz się informatyką? (t/n): ").lower() == 't'
gry = input("Czy lubisz grać w gry komputerowe? (t/n): ").lower() == 't'
instagram = input("Czy masz konto na Instagramie? (t/n): ").lower() == 't'

print("\nWYNIKI ANKIETY")
print(f"Zainteresowanie informatyką: {'Tak' if informatyka else 'Nie'}")
print(f"Granie w gry komputerowe: {'Tak' if gry else 'Nie'}")
print(f"Posiadanie konta na Instagramie: {'Tak' if instagram else 'Nie'}")
