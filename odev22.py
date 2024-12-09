# Vize ve final notlarını al
vize1 = float(input("1. Vize notunu giriniz: "))
vize2 = float(input("2. Vize notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

# Ortalama hesapla
ortalama = (vize1 * 0.2) + (vize2 * 0.2) + (final * 0.6)

# Harf notunu belirle
if (90 <= ortalama <= 100):
    harf_notu = "AA"
elif (80 <= ortalama < 90):
    harf_notu = "BA"
elif (70 <= ortalama < 80):
    harf_notu = "BB"
elif (60 <= ortalama < 70):
    harf_notu = "CB"
elif (50 <= ortalama < 60):
    harf_notu = "CC"
elif (40 <= ortalama < 50):
    harf_notu = "DC"
else:
    harf_notu = "FF"

# Sonucu yazdır
print(f"Ortalama: {ortalama:.2f}")
print(f"Harf Notu: {harf_notu}")