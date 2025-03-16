# Kullanıcıdan alının sayı asal mı değil mi, kontrol edelim.

sayi = int(input('Sayı giriniz: '))

if sayi < 2:
    print('2 den küçük sayıların asallık kontrolü yapılmaz..!')
else:
    is_prime = True

    sayac = 2
    while sayac < sayi:
        if sayi % sayac == 0:
            is_prime = False
            break
        sayac += 1

    if is_prime:  # is_prime == True
        print(f'{sayi} asaldır..!')
    else:
        print(f'{sayi} asal değildir..!')
