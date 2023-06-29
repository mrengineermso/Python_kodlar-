'''
sayilar=[1,2]
sayilar.append(ekle)
toplam=0
print("Hangi işlemi yapmak istiyorsunuz (toplam,ortalama,q,kucuksayi,buyuksayi): ")
islem = input()
  if islem == 'toplam':
    for eleman in range(0, len(sayilar)):
    ekle = input("sayi:")
    sayilar.append(ekle)
    toplam = toplam + sayilar[eleman]
    print("sayiların toplamı:",toplam)'''
sayac=0
liste = []
while 1:
    a = float(input("bir sayı giriniz"))
    liste.append(a)             #listeye tekrar ekle
    sayac+=1
    i=0                             #dizinin elemanlarını en baştan tekrar yazmak için sıfırladık
    print(liste[i])             #dizinin i indisindeki değerindeki elemanını yaz
    i+=1