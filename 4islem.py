def toplama(x, y):
    return x + y

def cıkarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    return x / y

while True:
 print("Yapılacak İşlemi Seçin.")
 print("1.Toplama")
 print("2.Çıkarma")
 print("3.Çarpma")
 print("4.Bölme")
 print("çıkmak için q harfine basınız")
 secim = input("Seçiminiz (+/-/3*///q):")

 sayi1 = int(input("1. Sayı: "))
 sayi2 = int(input("2. Sayı: "))

 if secim == '1':
    print(sayi1, "+", sayi2, "=", toplama(sayi1, sayi2))

 elif secim == '2':
    print(sayi1, "-", sayi2, "=", cıkarma(sayi1, sayi2))

 elif secim == '3':
    print(sayi1, "*", sayi2, "=", carpma(sayi1, sayi2))

 elif secim == '4':
    print(sayi1, "/", sayi2, "=", bolme(sayi1, sayi2))
 elif secim =='q':
    print("programdan çıktınız")
    break
