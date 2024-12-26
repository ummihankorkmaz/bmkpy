class BankaHesabi:
    def __init__(self, hesapSahibi):
        self.hesapSahibi = hesapSahibi
        self.bakiye = 0.0
    
    def paraYatir(self, miktar):
        self.bakiye += miktar
        return self.bakiye
    
    def paraCek(self, miktar):
        if miktar > self.bakiye:
            return "Yetersiz bakiye"
        self.bakiye -= miktar
        return self.bakiye

hesap = BankaHesabi("Ümmihan Korkmaz")
print(hesap.hesapSahibi)
print(hesap.bakiye)
print(hesap.paraYatir(1000))
print(hesap.paraCek(3000))