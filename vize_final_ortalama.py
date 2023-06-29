print("serhat"=="mustafa")
print(3<=5)
print(5<=5)
print("serhat"<="Serhat")
print("serhat"=="serhat" or 5==5)
print("serhat"=="sErhat"or 5==5)
print("serhat"=="serhat"or 5<=6)
print("serhat"=="serhat"and 5<=5)
yas=25
print(yas)
isim="serhat ozdemir"
print(isim)
durum=True
print(durum)
ders=input("ders adını giriniz")
not1 = input('Birinci notu giriniz')
not1 = int(not1)
not2 = int(input('İkinci notu giriniz: '))
sozlu=input('sözlü notunu giriniz:')
sozlu=int(sozlu)
ortalama=(not1+not2)/2
gecmenotu=(ortalama*0.7)+(sozlu*0.3)
if(gecmenotu<45):
    print(ders,'dersinden 1 ile kaldı', 'notu',gecmenotu)
elif(45<=gecmenotu<60):
    print(ders, 'dersinden 2 ile kaldı', 'notu', gecmenotu)
elif(60<=gecmenotu<70):
    print(ders,'dersinden 3 ile geçti', 'notu',gecmenotu)
elif (70 <= gecmenotu < 85):
    print(ders, 'dersinden 4 ile geçti', 'notu', gecmenotu)
elif (85 <= gecmenotu <= 100):
    print(ders, 'dersinden 5 ile geçti', 'notu', gecmenotu)