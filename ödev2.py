# Yakıt fiyatları (TL/Litre)
fiyatlar = {
    'benzin': 39.35,
    'dizel': 41.71,
    'lpg': 20.28
}

# Kullanıcıdan giriş al
yakıt_tipi = input("Yakıt tipi (benzin, dizel, lpg): ").lower()
mesafe = float(input("Mesafe (km): "))
yakıt_tüketimi = float(input("100 km'de tüketilen yakıt miktarı (litre): "))

# Yakıt masrafını hesapla
if yakıt_tipi in fiyatlar:
    yakıt_masrafı = (mesafe / 100) * yakıt_tüketimi * fiyatlar[yakıt_tipi]
    print(f"{mesafe} km mesafede {yakıt_tipi} yakıt masrafı: {yakıt_masrafı:.2f} TL")
else:
    print("Geçersiz yakıt tipi!")
