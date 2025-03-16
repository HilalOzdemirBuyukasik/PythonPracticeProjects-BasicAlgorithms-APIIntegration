#Bir restoranın menüsünde çeşitli yemekler var. Kullanıcıdan bir yemek adı alacak ve bu yemeğe göre fiyatını veya özel bir mesajı ekrana yazdıracak bir Python programı yaz.

#Menü:

#"Hamburger" → Fiyat: 50 TL

#"Pizza" → Fiyat: 80 TL

#"Makarna" → Fiyat: 40 TL

#"Salata" → Fiyat: 30 TL

#"Kebap" → Fiyat: 60 TL

#Diğer yemekler için → "Maalesef bu yemek menüde yok."


yemek = input('İstediğiniz yemeği giriniz: ')
match yemek.lower():
    case 'hamburger':
        print('Hamburger fiyatı: 50 TL.')
    case 'pizza':
        print('Pizza fiyatı: 80 TL.')
    case 'makarna':
        print('Makarna fiyatı: 40 TL.')
    case 'salata':
        print('Salata fiyatı: 30 TL')
    case 'kebap':
        print('Kebap fiyatı: 60 TL.')
    case _ :
        print('Maalesef bu yemek menüde yok.')