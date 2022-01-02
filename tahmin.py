# 6_rakaml-_tahmin_oyunu

import random

# burada rakam içerisindeki sayilardan bilbakalım listesine 6 tane seçtirip ekrana yazdırıcak
rakam = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
bilbakalım = random.sample(rakam, k=6)
print("Bu altı rakamdan 4 tane seçiniz\n==> ", bilbakalım, "<==")
print("****************************************", "\n")

# gizli_sayi ise bilbakalım içreisindeki sayılardan en fazla 2 tane aynı olmak üzere seçim yapıp list metodu ile liste haline dönüştürüyor
gizli_sayi = random.sample(bilbakalım, k=4)
gizli_sayi = list(gizli_sayi)

sayac = 0  # kullanıcı 13 tahminde bulamaz ise oyun kapanır
while sayac <= 12:
    sayac += 1

    # buradaki try-except ile eğer bir index hatası oluşursa bu hatayı oyunu kapatmadan söyleyip devam edicek
    try:
        tahmin = input("---> 4 basamaklı bir sayi giriniz--->")
        tahmin = list(tahmin)
    except IndexError:
        print("!!!lütfen 4 basamklı bir sayi giriniz!!!")

    # eğer tahmin listesinde eleman uzunluğu 4 ise oyun içerisine girer ama değil ise bir daha seçim yaptırır.
    if len(tahmin) == 4:

        # tahmininiz gizli_sayiya eşit ise kazandınız mesajı ile oyunu  kapatır
        if tahmin == gizli_sayi:
            print("*** KAZANDINIZ ***")
            break

        # tahmin gizli_sayiya eşit değil ise else'in içine girer
        else:
            D, Y = 0, 0

            for j in range(4):

                # burada karşılaştırmada rakam haricinde bir şey girilirse oyun kapanmadan hata verilir ve yeni bir sayi seçtirilir.
                try:
                    if tahmin[j] == gizli_sayi[j]:
                        print("{} sayısı dogru.".format(tahmin[j]))
                        D += 1

                    # tahminde girilen sayi eğer gizli_sayi'nin içinde varsa ama yeri değişikse alttaki mesaji verir.
                    elif tahmin[j] in gizli_sayi:
                        Y += 1
                        print("{} doğru ama yeri yanlış".format(tahmin[j]))

                except IndexError:
                    print("!!! hatalı tahmin'de bulundunuz!!!")

        # ve her denemede kaçıncı tahminde olduğumuzu gösterir birde doğru ise kaç tane doğru olduğunu yazdırır.
        print("Tahmin: {}".format(sayac))
        print("Doğru: " + str(D) + "\nYanlış: " + str(Y))

    # if len(tahmin) == 4 teki koşul sağlamıyor ise bir defa daha seçtirir.
    else:
        print("!!! 4 basmaklı bir sayi giriniz!!!")
        print("Tahmin: {}".format(sayac))

