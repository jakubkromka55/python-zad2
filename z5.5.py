# Sumuje liczby wprowadzone przez użytkownika i oblicza ich średnią arytmetyczną

total_sum = 0
count = 0  # Licznik wprowadzonych liczb

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Zakończenie wprowadzania liczb
    total_sum += number
    count += 1  # Zwiększenie licznika

if count > 0:
    average = total_sum / count
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The average of the numbers is: {average}")
else:
    print("No numbers were entered.")
