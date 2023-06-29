sayi = int(input("Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz:"))
faktöriyel = 1

if sayi >= 0:
    for i in range(1, sayi + 1):
        faktöriyel = faktöriyel * i
    print("Girdiğiniz sayının faktöriyeli:", faktöriyel)
else:
    print("Negatif sayıların faktöriyeli olmaz!")