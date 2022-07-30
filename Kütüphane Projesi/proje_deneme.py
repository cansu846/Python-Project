import time

from kutuphane import *
print("""
****** İşlemler *******
1.Kitapları Göster
2.Kitap Sorgulama
3.Kitap Ekle
4.Kitap Sil
Çıkmak için q'ya basınız
""")
kitap = Kitap("Otomatik Portakal", "Anthony Burges","Palme", 300)
kutuphane = Kutuphane();
while True:
    islem = input("İşlem seçiniz: ")
    if(islem=='q'):
        print("Programdan çıkılıyor...")
        break
    elif(islem=='1'):
        kutuphane.kitaplari_goster()
    elif(islem=='2'):
        kitap_ismi = input("Aradığınız kitap ismini giriniz: ")
        print("Kitap sorgulanıyor...")
        time.sleep(2)
        kutuphane.kitap_sorgula(kitap_ismi)
    elif (islem == '3'):
        isim = input("İsim giriniz: ")
        yazar_adi = input("Yazar adı: ")
        yayinevi = input("Yayınevi giriniz: ")
        sayfa_sayisi = int(input("Sayfa sayısı giriniz: "))
        kitap = Kitap(isim, yazar_adi, yayinevi, sayfa_sayisi)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kutuphane.kitap_ekle(kitap)
        print("Kitap başarıyla eklendi..")
    elif (islem == '4'):
        isim = input("Silmek istediğiniz kitap ismini giriniz: ")
        cevap = input("Emin misiniz(Evet=e, Hayır=h): ")
        if(cevap=='e'):
            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap başarıyla silindi..")
    else:
        print("Gecersiz işlem ....")





