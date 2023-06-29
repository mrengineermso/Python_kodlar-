import math
toplam=0
while True:
    sayi=input("Bir tam sayi giriniz: ")
    if sayi=="q":
        break
    sayi=float(sayi)
    if sayi<0:
        sayi=abs(sayi)
        toplam=toplam+sayi
        print(toplam)
    else:
        toplam=toplam+sayi
        print(toplam)