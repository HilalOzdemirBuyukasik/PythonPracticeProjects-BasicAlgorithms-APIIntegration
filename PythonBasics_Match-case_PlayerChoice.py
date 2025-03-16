#Bir oyun yapmak istiyorsun. Oyuncuya bir karakter seçtireceksin ve bu karakterin özelliklerini match-case yapısıyla ekrana yazdıracaksın. Program, kullanıcıdan sürekli olarak bir karakter adı girmesini istesin ve kullanıcı çıkmak istediğinde q tuşuna basarak programdan çıkabilsin.
#Karakterler:

#"Savaşçı" → Özellik: "Yüksek can, güçlü saldırı"

#"Büyücü" → Özellik: "Düşük can, güçlü büyüler"

#"Okçu" → Özellik: "Orta can, hızlı saldırı"

#"Şifacı" → Özellik: "Yüksek can, iyileştirme yetenekleri"

#Diğer karakterler için → "Geçersiz karakter seçimi!"

while True:
    karakter = input('Bir karakter seçin (Savaşçı, Büyücü, Okçu, Şifacı) veya oyundan çıkmak için "q" tuşuna basın: ')

    if karakter.lower() == 'q':
        print('Oyundan çıkılıyor..!')
        break
    match karakter.lower():
        case 'savaşçı':
            print('Savaşçı Özellikleri: "Yüksek can, güçlü saldırı"')
        case 'büyücü':
            print('Büyücü Özellikleri: "Düşük can, güçlü büyüler"')
        case 'okçu':
            print('Okçu Özellikleri: "Orta can, hızlı saldırı"')
        case 'şifacı':
            print('Şifacı Özellikleri: "Yüksek can, iyileştirme yetenekleri"')
        case _:
            print('Geçersiz karakter seçimi!')