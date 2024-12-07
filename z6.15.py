# Program sprawdzający numer EAN-13

ean = input("Wprowadź numer artykułu EAN-13: ")

if len(ean) == 13 and ean.isdigit():
    print("Numer artykułu jest poprawny")
    if ean[:3] == "590":
        print("Artykuł wyprodukowany w Polsce")
else:
    print("Numer artykułu jest niepoprawny")
