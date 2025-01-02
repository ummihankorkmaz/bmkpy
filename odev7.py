urunler = []


def urunEkle(name, price):
    urunler.append({'id': len(urunler) + 1, 'name': name, 'price': price})
    return f"Ürün eklendi: {name}, Fiyat: {price} TL"

def urunGuncelle(id, new_name, new_price):
    for urun in urunler:
        if urun['id'] == id:
            urun['name'] = new_name
            urun['price'] = new_price
            return f"Ürün güncellendi: {new_name}, Yeni Fiyat: {new_price} TL"
    return "Ürün bulunamadı!"

def urunleriGetir():
    return urunler


print(urunEkle("iphone 15", 60000))

print(urunGuncelle(1, "iphone 15 pro", 80000))

print(urunleriGetir())
