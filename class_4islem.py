class Hesapla():
    def toplama(self, a, b):
        return a + b
    def cikarma(self, a, b):
        return a - b
    def carpma(self, a, b):
        return a * b
    def bolme(self, a, b):
        return a / b
while True:
 karakter=input('Çıkmak için q ya basınız')
 if(karakter=='q'):
    break
 islem = int(input("İşlem giriniz : "))
 islem=Hesapla()
 a = int(input("Birinci sayiyi giriniz : "))
 b = int(input("İkinci sayiyi giriniz : "))
 if(islem=='+'):
     print(islem.topla(a,b))
 if (islem == '-'):
     print(islem.cikarma(a, b))
 if(islem=='*'):
     print(islem.carpma(a,b))
 if(islem=='/'):
        print(islem.bolme(a,b))
