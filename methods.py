# class
class Product:
    #method
    #attribute, property
    def __init__(self, name, price, isActive): #constructor
        self.name = name
        self.price = price
        self.isActive = isActive
    #instance method
    def intro(self):
          return f"ürün adı: {self.name} fiyat: {self.kdv_price()}"
    def kdv_price(self):
          return self.price * 1.18

# instance, Object
p1 = Product("Samsung A25", 70000, True)
p2 = Product("iPhone 17", 150000, True)
p3 = Product("Redmi 15", 20000, True)

urunler = [p1, p2, p3]

for urun in urunler:
    if urun.isActive:
        print(urun.intro())