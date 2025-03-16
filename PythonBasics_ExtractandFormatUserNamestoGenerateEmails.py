#Extract and Format User Names to Generate Emails

users = ['burak yaman',' ertuğrul', 'hakan bear yılmaz', 'kerim abdul cabbar ökkeş', 'murat     ', 'hil_al özdemir büyükaşık', '_pınar', 'egemen_ mustafa ulu']

import re

mail_address = []

for user in users:
    user = user.replace('_', '')
    user = ' '.join(user.split())

    user_names = user.split(' ')

    user_names = [item for item in user_names if item != '']

    if len(user_names) >= 2:
        mail_addres = f'{user_names[0]}.{user_names[-1]}@outlook.com'
        mail_address.append(mail_addres)

print(mail_address)