#Bu Python kodu, bir öğrencinin 3 dersinin notlarını alarak ortalamasını hesaplar ve başarı durumunu harf notu ile belirtir. Kullanıcıdan alınan ders notlarına göre öğrencinin başarılı, ortalama, geçer veya başarısız olduğunu gösteren bir sonuç çıkarır.
#This Python code takes a student's grades for 3 subjects, calculates the average, and indicates the success status with a letter grade. Based on the grades entered by the user, it generates a result showing whether the student is successful, average, passing, or failing.

def ogrenci_notu_hesapla():
    ad = input('Öğrenci adı: ')
    soyad = input('Öğrenci soyadı: ')

    ders1 = int(input('Ders 1 notu: '))
    ders2 = int(input('Ders 2 notu: '))
    ders3 = int(input('Ders 3 notu: '))

    ortalama = (ders1 + ders2 + ders3) / 3

    if ortalama >= 85:
        sonuclar = 'A (Başarılı)'
    elif ortalama >= 70:
        sonuclar = 'B (Ortalama)'
    elif ortalama >= 50:
        sonuclar = 'C (Geçer)'
    else:
        sonuclar = 'F (Başarısız)'

    print(f'\nÖğrenci: {ad} {soyad}')
    print(f'Ders 1: {ders1}, Ders 2: {ders2}, Ders 3: {ders3}')
    print(f'Ortalama: {ortalama:.2f}')
    print(f'Sonuç: {sonuclar}')

ogrenci_notu_hesapla()

#Bu Python kodu, belirli bir listedeki öğrencinin ders notlarını alarak her birinin ortalamasını hesaplar ve başarı durumlarını harf notu ile belirtir. Öğrencilerin adları, soyadları, ders notları ve sonuçları ekrana yazdırılır.
#This Python code takes the grades of students from a specific list, calculates the average for each, and indicates their success status with a letter grade. The students' names, surnames, grades, and results are printed on the screen.

def ogrenci_notu_hesapla():
    ogrenciler = [
        {'ad': 'Ahmet', 'soyad': 'Yılmaz', 'ders1': 90, 'ders2': 80, 'ders3': 70},
        {'ad': 'Mehmet', 'soyad': 'Kara', 'ders1': 60, 'ders2': 55, 'ders3': 65},
        {'ad': 'Ayşe', 'soyad': 'Demir', 'ders1': 85, 'ders2': 92, 'ders3': 88},
        {'ad': 'Zeynep', 'soyad': 'Çelik', 'ders1': 45, 'ders2': 50, 'ders3': 48}
    ]

    for ogrenci in ogrenciler:
        ad = ogrenci['ad']
        soyad = ogrenci['soyad']
        ders1 = ogrenci['ders1']
        ders2 = ogrenci['ders2']
        ders3 = ogrenci['ders3']

        ortalama = (ders1 + ders2 + ders3) / 3

        if ortalama >= 85:
            sonuclar = 'A (Başarılı)'
        elif ortalama >= 70:
            sonuclar = 'B (Ortalama)'
        elif ortalama >= 50:
            sonuclar = 'C (Geçer)'
        else:
            sonuclar = 'F (Başarısız)'

        print(f'\nÖğrenci: {ad} {soyad}')
        print(f'Ders 1: {ders1}, Ders 2: {ders2}, Ders 3: {ders3}')
        print(f'Ortalama: {ortalama:.2f}')
        print(f'Sonuç: {sonuclar}')

ogrenci_notu_hesapla()