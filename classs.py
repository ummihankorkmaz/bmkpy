# class isimleri her zaman büyük harfle başlar. Her bir classın belli özellikleri var classın içine 
# tanımladığımız özellikler method oluyor, class ürün instance ise oluşturduğumuz tüm ürünler.
class Product:
    pass
    #method
    #property

# instance, Object
p1 = Product()
p2 = Product()

sonuc = type(p1)
sonuc = type(p2)

sonuc = p1
sonuc = p2

print(sonuc)