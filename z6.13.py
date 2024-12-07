# Program sprawdzający prędkość samochodu na autostradzie

predkosc_samochodu = float(input("Wprowadź prędkość samochodu: "))
limit_predkosci_min = 40
limit_predkosci_max = 140

if predkosc_samochodu < limit_predkosci_min or predkosc_samochodu > limit_predkosci_max:
    print("Ostrzeżenie: nieprawidłowa prędkość samochodu!!")
