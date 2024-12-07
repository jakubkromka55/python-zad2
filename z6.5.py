# Program symulujący działanie termometru elektronicznego

temperature = 32

if temperature > 35:
    print("Jest bardzo gorąco")
elif temperature > 30:
    print("Jest gorąco")
elif temperature >= 15:
    print("Jest ciepło")
elif temperature >= 0:
    print("Jest zimno")
else:
    print("Uwaga, mróz")
