import time
from sarki import *

print("""
//// İŞLEMLER ////
1.Toplam Şarkı Süresi Hesaplama
2.Şarkı Ekleme
3.Şarkı Silme
Çıkış için q'ya basınız
""")
sarkilar = Sarkilar();
while True:
    islem = input("İşlem seçiniz: ")
    if(islem=="q"):
        print("Programdan çıkılıyor..")
        time.sleep(2)
        print("Yine bekleriz..")
    elif(islem=="1"):
        sarkilar.toplam_sarki_suresi()
    elif (islem == "2"):
        isim = input("Şarkı adı giriniz: ")
        sanatcı = input("Sanatçı  adını giriniz: ")
        produksyon = input("Prodüksyonu giriniz: ")
        album = input("Album adını giriniz: ")
        sarki_suresi = float(input("Şarkı suresini giriniz: "))
        sarki= Sarki(isim, sanatcı, album, produksyon, sarki_suresi)
        print("Şarkı ekleniyor..")
        time.sleep(2)
        sarkilar.sarki_ekle(sarki)
        print("Şarkı eklendi")
    elif (islem == "3"):
        isim = input("Silmek istediğiniz şarkı adını giriniz: ")
        cevap = input("Silmek istediğinize emin misiniz(Evet=e, Hayır=h): ")
        if(cevap=="e"):
            print("Şarkı siliniyor..")
            time.sleep(2)
            sarkilar.sarki_sil(isim)
            print("Şarkı silindi")
    else:
        print("Geçersiz işlem..")

