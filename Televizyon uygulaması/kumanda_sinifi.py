import random
import time
class Kumanda():
    def __init__(self, tv_durum="kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        self.tv_durum = tv_durum;
        self.tv_ses = tv_ses;
        self.kanal_listesi = kanal_listesi;
        self.kanal = kanal;
    def tv_ac(self):
        print("Tv açılıyor...");
        self.tv_durum = "Açık";
    def tv_kapat(self):
        print("Tv kapatılıyor...");
        self.tv_durum="Kapalı";
    def ses_ayarlari(self):
        while(True):
            cevap = input("Sesi arttır:'>'\nSesi azalt: '<'\nÇıkış: q");
            if(cevap=='>'):
                if(self.tv_ses!=32):
                    self.tv_ses+=1;
                    print("ses arttırıldı ses seviyesi: ", self.tv_ses);
                else:
                    print("Ses seviyesi en yüksek seviyede...");
            elif(cevap=='<'):
                if(self.tv_ses!=0):
                    self.tv_ses -= 1;
                    print("ses azaltıldı ses seviyesi: ", self.tv_ses);
                else:
                    print("Ses seviyesi en düşük seviyede...");
            else:
                print("Ses güncellendi: ", self.tv_ses);
                break;
    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1);
        self.kanal_listesi.append(kanal_ismi);
        print("Kanal eklendi");
    def rasgele_kanal_degistir(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1);
        self.kanal = self.kanal_listesi[rastgele];
        print("Şu anki kanal: ", self.kanal );
    def __len__(self):
        return len(self.kanal_listesi);
    def __str__(self):
        return "Tv durumu: {}\nTv ses: {}\nKanal listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal);
print("""
    **** Televizyon uygulaması ****
    1.Tv aç
    2.Tv kapat
    3.Ses ayarları
    4.Kanal ekle
    5.Kanal sayısını oğrenme
    6.Rastgele kanala geçme
    7.Televizyon bilgileri
    Çıkmak için q ya basınız...
    """);
kumanda = Kumanda();
while True:

    islem = input("İslem seçiniz: ");
    if (islem == '1'):
        kumanda.tv_ac();
    elif (islem == '2'):
        kumanda.tv_kapat();
    elif (islem == '3'):
        kumanda.ses_ayarlari();
    elif(islem=='4'):
        kanal_ismi = input("Kanal giriniz (Lütfen kanalları virgülle ayırarak giriniz or: Trt, kanal D) ");
        kanal_listesi = kanal_ismi.split(',');
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler);
    elif (islem == '5'):
        print(kumanda.__len__());
    elif (islem == '6'):
        kumanda.rasgele_kanal_degistir();
    elif (islem == '7'):
        print(kumanda.__str__());
    elif (islem == 'q'):
        print("Uygulamadan çıkılıyor...");
        break;
    else:
        print("Gecersiz işlem...");


