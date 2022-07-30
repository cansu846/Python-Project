import sqlite3
import time
class Kitap():
    def __init__(self, isim, yazar, yayinevi, sayfa_sayisi):
        self.isim =isim;
        self.yazar = yazar;
        self.yayinevi = yayinevi;
        self.sayfa_sayisi = sayfa_sayisi
    def __str__(self):
        return "Kitap ismi: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim, self.yazar, self.yayinevi,  self.sayfa_sayisi);
class Kutuphane():
    def __init__(self):
        self.baglanti_olustur();
    def baglanti_olustur(self):
        self.con = sqlite3.connect("kutuphane.db")
        self.cursor = self.con.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar(İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)"
        self.cursor.execute(sorgu)
        self.con.commit()
    def baglanti_kes(self):
        self.con.close()
    def kitaplari_goster(self):
        sorgu = "SELECT * FROM kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if (len(kitaplar)==0):
            print("Kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3])
                print(kitap);
    def kitap_sorgula(self, isim):
        sorgu = "SELECT * FROM kitaplar WHERE İsim=? "
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar)==0):
            print("Kitap bulunmuyor")
        for i in kitaplar:
            kitap = Kitap(i[0], i[1], i[2], i[3])
            print(kitap)
    def kitap_ekle(self,kitap):
        sorgu = "INSERT INTO Kitaplar VALUES(?, ?, ?, ?)"
        self.cursor.execute(sorgu, (kitap.isim, kitap.yazar, kitap.yayinevi, kitap.sayfa_sayisi))
        self.con.commit()
    def kitap_sil(self, isim):
        sorgu = "DELETE FROM kitaplar WHERE İsim=?"
        self.cursor.execute(sorgu, (isim,))
        self.con.commit()



