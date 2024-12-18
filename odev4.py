#1 ödev
def miyavlama():
    for i in range(2):
        print("miyav miyav")

miyavlama()

# 2 ödev
def dikdortgen_hesapla(uzun_kenar, kisa_kenar):
    alan = uzun_kenar * kisa_kenar
    cevre = 2 * (uzun_kenar + kisa_kenar)
    return alan, cevre

uzun_kenar = 72
kisa_kenar = 95
alan, cevre = dikdortgen_hesapla(uzun_kenar, kisa_kenar)

print(f"Dikdörtgenin Alanı: {alan}")
print(f"Dikdörtgenin Çevresi: {cevre}")



# 3 ödev
import random
def yazi_tura():
    sonuc = random.choice(['Yazı', 'Tura'])
    return sonuc

sonuc = yazi_tura()
print(f"Sonuç: {sonuc}")

# 4 ödev
def asal_sayilar_bul(baslangic, bitis):
    asal_sayilar = []
    for sayi in range(baslangic, bitis + 1):
        if sayi > 1:  # 1 sayısı asal sayı olmadığından kontrol ediliyor
            for i in range(2, sayi):
                if (sayi % i) == 0:
                    break
            else:
                asal_sayilar.append(sayi)
    return asal_sayilar

baslangic = 10
bitis = 50
asal_sayilar = asal_sayilar_bul(baslangic, bitis)
print(f"{baslangic} ile {bitis} arasındaki asal sayılar: {asal_sayilar}")


# 5 odev
def tam_bolenler_bul(sayi):
    tam_bolenler = [i for i in range(1, sayi + 1) if sayi % i == 0]
    return tam_bolenler

sayi = 28
bolenler = tam_bolenler_bul(sayi)
print(f"{sayi} sayısının tam bölenleri: {bolenler}")
