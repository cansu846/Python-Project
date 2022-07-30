import sqlite3
import time
class Sarki():
    def __init__(self, sarki_ismi, sanatci, album, produksiyon_sirketi, sarki_suresi):
        self.sarki_ismi = sarki_ismi
        self.sanatci = sanatci
        self.album = album
        self.produksiyon_sirketi = produksiyon_sirketi
        self.sarki_suresi = sarki_suresi
class Sarkilar():
    import sqlite3
    import time
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.con = self.sqlite3.connect("sarkilar.db")
        self.cursor = self.con.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS sarkilar(Şarkı_adı TEXT, Sanatçı TEXT, Albüm TEXT, Prodüksyon_şirketi TEXT, Şarkı_süresi FLOAT)"
        self.cursor.execute(sorgu)
    def baglanti_kapat(self):
        self.con.close()

    def toplam_sarki_suresi(self):
        sorgu = "SELECT Şarkı_süresi FROM sarkilar"
        self.cursor.execute(sorgu)
        sure_listesi = self.cursor.fetchall()
        toplam = 0
        for i in sure_listesi:
            i = list(i)
            i = str(i)
            i = i.lstrip("[")
            i = i.rstrip("]")
            liste = i.split(".")
            dk = int(liste[0])
            sn = int(liste[1])
            toplam += dk * 60 + sn
        if(toplam==0):
            print("Henüz şarkı bulunmamakta..")
        else:
            print("Sarkilar listesinde bulunan toplam sarki süresi:", toplam, "sn dir")

    def sarki_ekle(self, sarki):
        sorgu = "INSERT INTO sarkilar VALUES(?, ?, ?, ?, ?)"
        self.cursor.execute(sorgu, (sarki.sarki_ismi, sarki.sanatci, sarki.album, sarki.produksiyon_sirketi, sarki.sarki_suresi))
        self.con.commit()

    def sarki_sil(self, isim):
        sorgu = "DELETE FROM sarkilar WHERE Şarkı_adı=?"
        self.cursor.execute(sorgu, (isim,))
        self.con.commit()
