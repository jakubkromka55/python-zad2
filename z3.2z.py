# Program sprawdzający poprawność loginu i hasła

login = 'joe'  # Poprawny login
password = 'abcd'  # Poprawne hasło

# Pobranie loginu i hasła od użytkownika
entered_login = input('Login: ')
entered_password = input('Hasło: ')

# Sprawdzenie, czy login i hasło są poprawne
if login == entered_login and password == entered_password:
    print('Zalogowano pomyślnie')
else:
    print('Niepoprawny login lub hasło!')
