# Program określający, w której ćwiartce układu współrzędnych znajduje się punkt P(x, y)

x = float(input("Podaj współrzędną x: "))
y = float(input("Podaj współrzędną y: "))

if x == 0 and y == 0:
    print("Punkt P(0,0) leży w punkcie początkowym układu współrzędnych")
elif x == 0:
    print("Punkt P leży na osi Y")
elif y == 0:
    print("Punkt P leży na osi X")
elif x > 0 and y > 0:
    print(f"Punkt P({x},{y}) leży w pierwszej ćwiartce układu współrzędnych")
elif x < 0 and y > 0:
    print(f"Punkt P({x},{y}) leży w drugiej ćwiartce układu współrzędnych")
elif x < 0 and y < 0:
    print(f"Punkt P({x},{y}) leży w trzeciej ćwiartce układu współrzędnych")
else:
    print(f"Punkt P({x},{y}) leży w czwartej ćwiartce układu współrzędnych")
