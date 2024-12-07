# Program obliczający całkowity czas prania w pralce

produkt_do_prania = input('Wybierz program prania: (j)acket, (u)nderwear, (s)hoes: ').lower()
płukanie = input('Dodatkowe płukanie? (y/n): ').lower() == 'y'
wirowanie = input('Dodatkowe wirowanie? (y/n): ').lower() == 'y'

total_washing_time = 0

if produkt_do_prania == 'j':
    total_washing_time += 40
elif produkt_do_prania == 'u':
    total_washing_time += 70
elif produkt_do_prania == 's':
    total_washing_time += 20

if płukanie:
    total_washing_time += 15
if wirowanie:
    total_washing_time += 9

print(f"Całkowity czas prania: {total_washing_time} minut")
