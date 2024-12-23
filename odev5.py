# Hesap bilgilerini tutmak için bir dictionary oluşturuyoruz.
hesap = {
    "bakiye": 60,
    "ek_hesap": 5000
}

def menu():
    print("\nHoşgeldiniz!")
    print("1. Bakiye Sorgula")
    print("2. Para Çekme")
    print("3. Para Yatırma")
    print("4. Çıkış")
    secim = input("Seçiminizi yapınız: ")
    return secim

def bakiyeSorgula():
    print(f"Mevcut bakiye: {hesap['bakiye']} TL")
    print(f"Ek hesap: {hesap['ek_hesap']} TL")

def paraCekme():
    cekilecek_miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
    if cekilecek_miktar <= hesap['bakiye']:
        hesap['bakiye'] -= cekilecek_miktar
        print(f"{cekilecek_miktar} TL çekildi. Yeni bakiye: {hesap['bakiye']} TL")
    else:
        toplam_bakiye = hesap['bakiye'] + hesap['ek_hesap']
        if cekilecek_miktar <= toplam_bakiye:
            kullan_ek_hesap = input("Bakiyeniz yetersiz. Ek hesap kullanılsın mı? (E/H): ")
            if kullan_ek_hesap.upper() == 'E':
                kullanilacak_ek_hesap = cekilecek_miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ek_hesap'] -= kullanilacak_ek_hesap
                print(f"{cekilecek_miktar} TL çekildi. Yeni bakiye: {hesap['bakiye']} TL, Ek hesap: {hesap['ek_hesap']} TL")
            else:
                print("İşlem iptal edildi.")
        else:
            print("Yetersiz bakiye ve ek hesap.")

def paraYatirma():
    yatirilacak_miktar = int(input("Yatırmak istediğiniz miktarı giriniz: "))
    hesap['bakiye'] += yatirilacak_miktar
    print(f"{yatirilacak_miktar} TL yatırıldı. Yeni bakiye: {hesap['bakiye']} TL")

def bankamatik():
    while True:
        secim = menu()
        if secim == '1':
            bakiyeSorgula()
        elif secim == '2':
            paraCekme()
        elif secim == '3':
            paraYatirma()
        elif secim == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

# Bankamatik uygulamasını başlat
bankamatik()
