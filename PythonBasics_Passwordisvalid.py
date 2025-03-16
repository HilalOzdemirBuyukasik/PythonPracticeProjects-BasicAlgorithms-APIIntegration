#Turkish language below
#password is valid?
#en az 16 karakteri olacak
#en az 1 büyük harf, bir küçük harf içerecek
#en az 1 noktalama işareti içerecek
#en az 1 rakam içerecek
#bunlara uymuyorsa invalid password

import string

password = input('Lütfen şifrenizi giriniz: ')

uzunluk_gecerli = len(password) >= 16
buyuk_harf_var = any(c.isupper() for c in password)
kucuk_harf_var = any(c.islower() for c in password)
rakam_var = any(c.isdigit() for c in password)
noktalama_var = any(c in string.punctuation for c in password)

if uzunluk_gecerli and buyuk_harf_var and kucuk_harf_var and rakam_var and noktalama_var:
    print("Geçerli şifre!")
else:
    print("Geçersiz şifre!")

