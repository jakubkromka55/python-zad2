# Program sprawdzający, czy osoba jest dobrym influencerem na podstawie posiadanych kont

facebook = input("Czy masz konto na Facebooku? (t/n): ").lower() == 't'
twitter = input("Czy masz konto na Twitterze? (t/n): ").lower() == 't'
instagram = input("Czy masz konto na Instagramie? (t/n): ").lower() == 't'

if (facebook + twitter + instagram) >= 2:
    print("Jesteś dobrym influencerem!")
else:
    print("Nie jesteś dobrym influencerem.")
