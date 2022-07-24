def not_hesapla(satir):
    harf_notu = "";
    satir = satir[:-1];
    liste = satir.split(",");
    isim = liste[0];
    not1 = int(liste[1]);
    not2 = int(liste[2]);
    not3 = int(liste[3]);
    ort = not1*(3/10)+not2*(3/10)+not3*(4/10);
    if(ort>=90):
        harf_notu = "AA";
    elif(ort>=85):
        harf_notu="BA";
    elif(ort>=80):
        harf_notu="BB";
    elif(ort>=75):
        harf_notu="BC";
    elif (ort >= 70):
        harf_notu = "CC";
    elif (ort >= 65):
        harf_notu = "DC";
    elif (ort >= 60):
        harf_notu = "DD";
    elif (ort >= 55):
        harf_notu = "FD";
    else:
        harf_notu = "FF";
    return isim+"------------> "+harf_notu+"\n";


with open("dosya.txt","r",encoding="utf-8") as file:
    eklenecekler_listesi = [];

    for satir in file:
       eklenecekler_listesi.append( not_hesapla(satir));
    print(eklenecekler_listesi);
with open("notlar.txt", "w",encoding="utf-8") as file2:
    for i in eklenecekler_listesi:
        file2.write(i);
