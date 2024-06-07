#Boy Kilo Hesabı Uygulaması#Boy Kilo Hesabı Uygulaması
#Boyu yazarken diyelim boyu 169 cm ise bunu 1.69 diye yazarız
name=input("Lütfen adınızı giriniz: ")


kg= float(input("Lütfen kilonuzu giriniz: "))


hg= float(input("Lütfen boyunuzu giriniz: "))


hesaplama= (kg) / (hg**2)


zayif= (hesaplama>=0) and (hesaplama<=18.4)


normal= (hesaplama>18.4) and (hesaplama<=24.9)


kilolu= (hesaplama>24.9) and (hesaplama<=29.9)


obez= (hesaplama>29.9) and (hesaplama<=34.9)


if (hesaplama>=0) and (hesaplama<=18.4):
    print(f'{name} kilo hesabın : {hesaplama} ve kilo değerlendirmen zayıf ')
elif (hesaplama>18.4) and (hesaplama<=24.9) :
    print(f'{name} kilo hesabın : {hesaplama} ve kilo değerlendirmen normal ')
elif (hesaplama>24.9) and (hesaplama<=29.9) :
    print(f'{name} kilo hesabın : {hesaplama} ve kilo değerlendirmen kilolu ')
elif (hesaplama>29.9) and (hesaplama<=34.9) :
    print(f'{name} kilo hesabın : {hesaplama} ve kilo değerlendirmen obez ')
else:
    print("Bilgileriniz yanlış")
