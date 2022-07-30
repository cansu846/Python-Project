
def not_hesapla(satir):
   satir = satir[:-1]
   ogrenci_bilgi_liste = satir.split(":")
   ad_soyad = ogrenci_bilgi_liste[0]
   notlar = ogrenci_bilgi_liste[1]
   notlar = notlar.strip()
   notlar = notlar.split(",")
   not1 = int(notlar[0])
   not2 = int(notlar[1])
   not3 = int(notlar[2])
   ort = not1*(0.3) + not2*(0.3) + not3*(0.4)
   if(ort>=90 and ort<=100):
       harf = "AA"
   elif(ort>=85):
       harf = "BA"
   elif (ort>=80):
       harf = "BB"
   elif (ort>=75):
       harf = "CB"
   elif (ort>=65):
       harf = "CC"
   elif (ort >= 60):
       harf = "DC"
   elif (ort >= 55):
       harf = "DD"
   elif (ort >= 50):
       harf = "FD"
   elif (ort >= 0):
       harf = "FF"
   else:
       print("Gecersiz ortalama...")
       harf = "Gecersiz ortalama"
   return ad_soyad + ": " + harf + "\n"


def ortalama_oku():
    with open("notlar.txt", "r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir), end="")

def not_gir():
    isim = input("İsminizi giriniz: ")
    soyisim = input("Soyisminizi giriniz: ")
    not1 = input("1.Notunuzu giriniz: ")
    not2 = input("2.Notunuzu giriniz: ")
    not3 = input("3.Notunuzu giriniz: ")
    with open("notlar.txt","a", encoding="utf-8") as file:
        file.write(isim+" "+soyisim+": "+not1+","+ not2+","+not3+"\n")
def not_kaydet():
    with open("notlar.txt", "r", encoding="utf-8")as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))
    with open("sonuclar.txt", "w", encoding="utf-8")as file2:
        for i in liste:
            file2.write(i)
        print("Notlar başarıyla kaydedildi...")
print("""
    *****İşlemler*****
        1-Notları Oku
        2-Not Gir
        3-Notları kaydet
        Çıkış için q'ya basınız
    """)

while True:
    islem = input("İşlem seçiniz: ")
    if(islem=="1"):
        ortalama_oku()
    elif(islem=="2"):
        not_gir()
    elif(islem=="3"):
        not_kaydet()
    elif(islem=="q"):
        print("Programdan Çıkılıyor...")
        break
    else:
        print("Geçersiz işlem")