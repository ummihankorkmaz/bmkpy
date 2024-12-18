#Bir fonksiyon çalıştırılmayı bekleyen kod satırlarıdır. fonksiyon sadece çağırıldığında çalışır. parametreye göre çalıştırılır


#merhaba bmk yazısı range parantezindeki sayı kadar yazılıyor.
def selamlama():
    for i in range(2):
        print("merhaba BMK")

selamlama()

#toplam
def toplama():
    a = 10
    b = 20
    print(a+b)
toplama()

#toplam2
def toplam():
    return 10+20
sonuc= toplam()
print(sonuc)

#yaş hesaplama
def yil():
    import datetime
    return datetime.datetime.now().year

def saat():
    import datetime
    return datetime.datetime.now().hour

def yasHesapla():
    return yil() - 1983

print(yasHesapla())


#saate göre selam verme
def saat():
    import datetime
    return datetime.datetime.now().hour
def selamlama():
    if(saat() < 12):
        return "Günaydın"
    else :
        return "Merhaba"
print(selamlama())



#isimle selamlama
def selamlama(isim):
    return "Merhaba, " + isim
print(selamlama("Ummi"))

#toplam3
def toplam(sayi1, sayi2):
    return sayi1 + sayi2
print (toplam(20, 40))
print (toplam(10, 30))

#tekrar yas hesaplama ama daha iyi
def yil():
    import datetime
    return datetime.datetime.now().year
def yasHesapla(dogumYili):
    return yil() - dogumYili
print(yasHesapla(2005))

#emeklilik
def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    kalanSure = 65 - yas
    if kalanSure > 0:
        return f"{isim}, emekliliğinize {kalanSure} yıl kaldı." #f ten sonrası str yazı içindekini değiştiremiyorum. ama bu formatta yazsın diye öyle yaptık
    else:
        return f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz."  # abs int türündeki negatif sayıları pozitife çevirir.
print (emekliligeKacYilKaldi(1905, "ümmi")) 