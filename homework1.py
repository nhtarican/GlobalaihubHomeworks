adsoyad = input("Adınızı ve Soyadınızı Giriniz: ")
yas = int(input("Lütfen Yaşınızı Giriniz: "))
kg = float (input("Lütfen Kilonuzu Giriniz: "))
boy = float (input("Lütfen Boyunuzu Giriniz: (Örnek: 1.70) "))

index = (kg/ (boy ** 2))

zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu = (index > 24) and (index <= 29.9)
obez = (index > 29.9) 
a= type (adsoyad)
b= type(yas)
c= type(kg)
d= type(boy)

print (f'Sayın {adsoyad} Kilo Endeksiniz {index} Kilo Değerlendirmeniz ZAYIF: {zayif}')
print (f'Sayın {adsoyad} Kilo Endeksiniz {index} Kilo Değerlendirmeniz NORMAL: {normal}')
print (f'Sayın {adsoyad} Kilo Endeksiniz {index} Kilo Değerlendirmeniz KİLOLU: {kilolu}')
print (f'Sayın {adsoyad} Kilo Endeksiniz {index} Kilo Değerlendirmeniz OBEZ: {obez}')
print (f'adsoyad değişkenin tipi {a}\n yas değişkenin tipi {b}\n kg isimli değişkenin tipi {c}\n boy isimli değişkenin tipi {d}')





