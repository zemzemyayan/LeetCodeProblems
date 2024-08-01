# İlk on karakter yolcuların telefon numaralarından oluşmaktadır.
# Bir sonraki karakter kişinin cinsiyetini belirtir.
# Kişinin yaşını belirtmek için aşağıdaki iki karakter kullanılır.
# Son iki karakter o kişinin hangi koltuğa oturacağını belirler


# Giriş: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
#  Çıkış: 2
#  Açıklama: 0, 1 ve 2 indekslerindeki yolcuların yaşları 75, 92 ve 40'tır. Dolayısıyla, 60 yaşın üzerinde olan 2 kişi vardır.

# BİLGİ: 
# range(4) Python'da kullanılan bir fonksiyondur ve 0'dan başlayarak verilen sayıdan bir eksik olan sayıya kadar bir aralık oluşturur. Yani, range(4) ifadesi şu aralığı oluşturur: 0, 1, 2, 3. Bu aralık genellikle döngülerde kullanılır.

details = ["7868190130M7522","5303914400F9211","9273338290F4010","9273338290F5010","9273338290F7810","9273338290F5010","9273338290F7010"]
n=len(details)
sayac=0
print(n)
for i in details:
    yas=i[11]+i[12]
    print(yas)
    if(int(yas)>60):
        sayac=sayac+1

print(sayac,"kişi 60 yaş üzerindedir.")
