sayilar =  (3, 5, 7, 2, 12, 32, 45)
for sayi in sayilar:
    print(sayi)


for sayi in sayilar:
    if sayi %3 == 0:
        print(sayi)


toplam = sum(sayilar)
print(f"Toplam: {toplam}")