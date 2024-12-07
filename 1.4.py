# Terminal płatniczy w sklepie

account_balance = 500  # Saldo na koncie klienta
total_payment = float(input('Podaj łączną wartość zakupów (zł): '))
left = account_balance - total_payment
# Sprawdzenie, czy środki na koncie są wystarczające
if total_payment <= account_balance:  
    print('Płatność zrealizowana zostało', left)  # Potwierdzenie płatności
else:
    print('Brak środków na koncie')  # Informacja o niewystarczających środkach
