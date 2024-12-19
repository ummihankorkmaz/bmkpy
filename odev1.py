# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]

# 2- Liste kaç elemanlıdır?
eleman_sayisi = len(markalar)
print(f"Liste {eleman_sayisi} elemanlıdır.")

# 3- Listenin ilk ve son elemanı nedir?
ilk_eleman = markalar[0]
son_eleman = markalar[-1]
print(f"Listenin ilk elemanı: {ilk_eleman}")
print(f"Listenin son elemanı: {son_eleman}")

# 4- "Renault" markasını "Togg" ile güncelleyiniz.
markalar[2] = "Togg"
print(f"Yeni liste: {markalar}")

# 5- Togg
togg_var_mi = "Togg" in markalar
print(f"'Togg' listenin bir elemanı mıdır?: {togg_var_mi}")

# 6-"Ford" ve "Citroen"
markalar.append("Ford")
markalar.append("Citroen")
print(f"Listenin güncel hali: {markalar}")

# 7- Listenin son elemanı
markalar.pop()
print(f"Listenin son hali: {markalar}")

# 8- Öğrenci listesi oluşturma
ogrenciler = [
    ["Yiğit Bilgi", 2010, [70, 80, 90]],
    ["Ada Bilgi", 2011, [70, 70, 80]],
    ["Çınar Turan", 2017, [60, 60, 90]]
]

# 9- Öğrencilerin yaşlarını hesaplayınız.

from datetime import datetime

su_anki_yil = datetime.now().year

yaslar = [(su_anki_yil - ogrenci[1]) for ogrenci in ogrenciler]
print(f"Öğrencilerin yaşları: {yaslar}")

# 10- Öğrencilerin not ortalaması
not_ortalamalari = [sum(ogrenci[2]) / len(ogrenci[2]) for ogrenci in ogrenciler]
print(f"Öğrencilerin not ortalamaları: {not_ortalamalari}")
