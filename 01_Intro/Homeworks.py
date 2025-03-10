#Ödev: 6.3.2025,

users = ['burak yılmaz',' ertuğrul', 'hakan bear yılmaz', 'kerim abdul cabbar ökkeş', 'murat     ', 'hil_al özdemir büyükaşık', '_pınar', 'egemen_ kağan duman']

import re

mail_address = []

for user in users:
    # (Boşlukları ve alt çizgileri temizle)
    user = user.replace('_', '')  # Alt çizgileri kaldır
    user = ' '.join(user.split())  # Fazla boşlukları temizle

    # İsimleri boşluğa göre böl
    user_names = user.split(' ')

    # Boş elemanları listeden çıkar
    user_names = [item for item in user_names if item != '']

    if len(user_names) >= 2:
        mail_addres = f'{user_names[0]}.{user_names[-1]}@outlook.com'
        mail_address.append(mail_addres)

print(mail_address)

"""
Ödev 6.3.2025: password is valid?
en az 16 karakteri olacak
en az 1 büyük harf, bir küçük harf içerecek
en az 1 noktalama işareti içerecek
en az 1 rakam içerecek
bunlara uymuyorsa invalid password
"""

import string

password = input('Lütfen şifrenizi giriniz: ')

uzunluk_gecerli = len(password) >= 16
buyuk_harf_var = any(char.isupper() for char in password)
kucuk_harf_var = any(char.islower() for char in password)
rakam_var = any(char.isdigit() for char in password)
noktalama_var = any(char in string.punctuation for char in password)

if uzunluk_gecerli and buyuk_harf_var and kucuk_harf_var and rakam_var and noktalama_var:
    print("Geçerli şifre!")
else:
    print("Geçersiz şifre!")