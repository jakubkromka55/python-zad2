# Symulator bankomatu (ATM)

balance = 1000  # Początkowe saldo
pin = '1111'    # Początkowy 4-cyfrowy PIN

# Funkcja do sprawdzenia poprawności wprowadzonego PIN-u
def check_pin():
    entered_pin = input("Enter your PIN: ")
    return entered_pin == pin

# Funkcja do zmiany PIN-u
def change_pin():
    global pin
    while True:
        new_pin = input("Enter a new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            confirm_pin = input("Confirm the new PIN: ")
            if new_pin == confirm_pin:
                pin = new_pin
                print("PIN has been successfully changed.")
                break
            else:
                print("PINs do not match. Try again.")
        else:
            print("Invalid PIN. It must be exactly 4 digits. Try again.")

# Główna pętla programu
while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    print()

    if choice in {'1', '2', '3'}:
        if not check_pin():
            print("Incorrect PIN. Access denied.")
            continue

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        change_pin()
    elif choice == '5':
        print("Exiting... Thank you for using the ATM!")
        break  # Wyjście z pętli
    else:
        print("Invalid option. Please try again.")
