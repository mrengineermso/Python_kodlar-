while True:
    durum= input("İşlem Yapmak İster Misiniz? e/h")
    if(durum=="e"):
        islem=input("İşlemi giriniz:")
        sayi1=''
        sayi2=''
        girilen_islem=''
        for i in islem:
            if girilen_islem=='':
                if i=="+" or i=="-" or i=="*" or i=="/":
                    girilen_islem=i
                else:
                    sayi1+=i
            else:
                sayi2+=i
        sayi1=int(sayi1)
        sayi2=int(sayi2)

        sonuc=0
        if girilen_islem=="+":
            sonuc=sayi1+sayi2
        elif girilen_islem=="-":
            sonuc=sayi1-sayi2
        elif girilen_islem=="*":
            sonuc=sayi1*sayi2
        elif girilen_islem=="/":
            sonuc=sayi1/sayi2
        print(sonuc)
    elif(durum=='h'):
        break