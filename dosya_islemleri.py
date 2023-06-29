dosya=open('İsimler.txt','r')
"""for isim in dosya.reaalines()
    print(isim)"""
isimler=dosya.readlines()
for isim in isimler:
    print(isim)
print(len(isimler))
dosya_yaz=open('komek_liste.txt','w')
dosya_yaz.write('musa\n')
dosya_yaz.write('nihat\n')
dosya_yaz.write('aslıhan\n')
dosya_yaz.close()

dosya=open('komek_liste.txt','r+')
liste=dosya.readlines()
for i in liste:
    print(i)
dosya.write('Sude\n')
dosya