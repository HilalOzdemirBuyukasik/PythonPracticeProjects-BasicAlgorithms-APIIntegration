# This project is a simple flight ticket reservation system that allows users to log in, choose their travel details, and purchase tickets (one-way or round-trip). The system verifies user identity using the provided TC Kimlik number(ID number) and processes payment details to complete the booking. The app includes basic user authentication and dynamic ticket pricing based on the chosen departure and destination cities.

zeynep_account = {
    'ad' : 'zeynep',
    'soyad':'şahin',
    'tc kimlik no': '45678901234',
    'cinsiyet': 'kadın',
    'email': 'zeynep.sahin @ example.com',
    'şifre': 'Zeynep123!'
}

can_account = {
    'ad': 'can',
    'soyad': 'öztürk',
    'tc kimlik no': '56789012345',
    'cinsiyet': 'erkek',
    'email': 'can.ozturk@example.com',
    'şifre': 'can456',
}

aylin_account = {
    'ad': 'aylin',
    'soyad': 'çelik',
    'tc kimlik no': '67890123456',
    'cinsiyet': 'kadın',
    'email': 'aylin.celik@example.com',
    'şifre': 'Aylin789$',
}

users = [zeynep_account, can_account, aylin_account]

def login(email: str, pwd: str) -> dict:
    for user in users:
        if user['email'] == email and user['şifre'] == pwd:
            return user
    return {}

def get_travel_details() -> dict:

    departure_city = input('Çıkış şehrinizi yazın: ')
    destination_city = input('Varış noktanızı yazın: ')
    travel_date = input('Gidiş tarihinizi (yyyy-aa-gg formatında) yazın: ')

    return {
        'departure city': departure_city,
        'destination city': destination_city,
        'travel_date': travel_date
    }

def calculate_ticket_price(departure_city: str, destination_city: str) -> int:
    price = 0
    if departure_city.lower() == 'istanbul' and destination_city.lower() == 'ankara':
        price = 500
    elif departure_city.lower() == 'istanbul' and destination_city.lower() == 'izmir':
        price = 300
    elif departure_city.lower()  == 'ankara' and destination_city.lower()  == 'izmir':
        price = 400
    else:
        price = 600
    return price

def buy_ticket(ticket_price: int, ticket_type: str, user_tc: str) -> bool:
    if ticket_type == 'tek yön':
        print(f'Girdiğiniz tarihe göre bilet fiyatı {ticket_price} TLdir.')
    elif ticket_type == 'gidiş dönüş':
        total_price = ticket_price *  2
        print(f'Gidiş-dönüş biletinin fiyatı {total_price} TLdir.')
    else:
        print('Geçersiz bilet tipi seçildi.')
        return False

    purchase = input('Satın almak istiyor musunuz? (Evet / Hayır): ').lower()

    if purchase == 'evet':
        print('Lütfen kimlik bilgilerinizi giriniz: ')
        ad = input('Ad: ')
        soyad = input('Soyad: ')
        input_tc = input('Lütfen TC Kimlik numaranızı giriniz: ')
        cinsiyet = input('Cinsiyet (Kadın/Erkek): ')

        if input_tc != user_tc:
            print('Girilen TC Kimlik numarası hatalı. Bilet satın alma işlemi iptal edildi.')
            return False

        print('\nLütfen ödeme bilgilerinizi giriniz: ')
        kredi_karti_no = input('Kredi kartı numarası: ')
        son_kullanma_tarihi = input('Son kullanma tarihi (MM/YY): ')
        ccv_kodu = input('CCV Kodu: ')

        print('\nKimlik ve ödeme bilgileri doğrulandı. Bilet satın alındı, teşekkürler!')

        final_price = ticket_price if ticket_type == 'tek yön' else ticket_price * 2
        print(f'Bilet sahibi: {ad} {soyad}\nBilet Fiyatı: {final_price} TL\n')
        return True
    else:
        print('Bilet satın alma iptal edildi.')
        return False


def trip_choice() -> str:
    trip_type = input('Tek yön bilet mi yoksa gidiş-dönüş mü almak istersiniz? (Tek yön / Gidiş Dönüş): ')

    while trip_type.lower() not in ['tek yön', 'gidiş dönüş']:
        print('Lütfen geçerli bir seçenek girin: Tek yön veya Gidiş-Dönüş')
        trip_type = input('Tek yön bilet mi yoksa gidiş-dönüş mü almak istersiniz? (Tek yön / Gidiş Dönüş): ')

    return trip_type


def main():

    email = input('Email: ')
    password = input('Şifre: ')

    user_account = login(email, password)

    if user_account != {}:
        print(f'Hoşgeldiniz, {user_account['ad']} {user_account['soyad']}')

        travel_details = get_travel_details()
        ticket_type = trip_choice()
        ticket_price = calculate_ticket_price(travel_details['departure city'], travel_details['destination city'])
        buy_ticket(ticket_price, ticket_type, user_account['tc kimlik no'])

    else:
        print('Bilgilerinizi yanlış girdiniz.')


main()