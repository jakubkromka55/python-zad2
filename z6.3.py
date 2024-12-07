# Oświetlenie w domu z trzema żarówkami i dwoma przełącznikami
# Sprawdzenie, ile żarówek się świeci

light_switch1 = False  # False - wyłączony, True - włączony
light_switch2 = False
bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2

print(f"Liczba zapalonych żarówek: {bulbs_on}")
