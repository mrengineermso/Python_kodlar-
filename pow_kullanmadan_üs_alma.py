def mutlakdeger(sayi):
    if sayi<0:
        sayi=sayi*(-1)
    return sayi
print(mutlakdeger(-58))

def usalma(taban,us=2):
    i=0
    sonuc=1
    while i < us:
        i += 1
        sonuc = sonuc * taban
    return sonuc

print(usalma(5))
print(usalma(5,1))
print((usalma(5,5)))