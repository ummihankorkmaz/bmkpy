urunler = ["iphone 13","samsung s24","samsung a25","iphone 15","iphone 14"]

# iPhone marka ürünleri listeleme
iphone_urunler = [urun for urun in urunler if urun.find("iphone") != -1]

print("iPhone Ürünleri:")
for urun in iphone_urunler:
    print(urun)


# Samsung ürünlerini sayma
samsung_sayisi = sum(1 for urun in urunler if urun.find("samsung") != -1)

print(f"Samsung ürün sayısı: {samsung_sayisi}")
