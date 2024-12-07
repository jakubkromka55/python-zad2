# Walidator hasła
# Nowe hasło musi mieć co najmniej 12 znaków

new_password = input('Podaj nowe hasło: ')
if len(new_password) < 12:
    print('Hasło jest za krótkie (min. 12 znaków).')
else:
    print('Hasło jest wystarczająco silne.')
