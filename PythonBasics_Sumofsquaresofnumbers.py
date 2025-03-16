#1 ile 50 arasındaki sayıların karelerini hesaplayıp, bu karelerin toplamını bulunuz. Ayrıca, bu karelerden kaç tanesinin çift sayı olduğunu da hesaplayınız.

sayac = 1
ciftlerin_kareleri_toplami = 0
teklerin_kareleri_toplami = 0
cift_karelerin_sayisi = 0

while sayac <= 50:
    kare = sayac ** 2
    if sayac % 2 == 0:
        ciftlerin_kareleri_toplami += kare
        cift_karelerin_sayisi += 1
    else:
        teklerin_kareleri_toplami += kare
    sayac += 1

print(f'Çiftlerin Kareleri Toplamı: {ciftlerin_kareleri_toplami}')
print(f'Teklerin Kareleri Toplamı: {teklerin_kareleri_toplami}')
print(f'Çift Karelerin Sayısı: {cift_karelerin_sayisi}')