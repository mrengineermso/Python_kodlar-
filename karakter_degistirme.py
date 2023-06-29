metin = input("Bir metin girişi yapınız: ")
metin=metin.replace(" ","-")
print(metin)

değistirilecek(metin)
degistir = input('Değiştirilecek kelimeyi giriniz')
index = string.find(metin, degistir)
degistir