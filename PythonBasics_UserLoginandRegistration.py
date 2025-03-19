import string

users = [
    ('moonlord', '098'),
    ('starrider', '765'),
    ('butterfly', '432'),
]

def sign_in(username: str, password: str) -> str:
    for userName, pwd in users:
        if userName == username and pwd == password:
            return f'{userName} hoş geldiniz'

    return 'hatalı giriş yaptınız..!'

def sign_up(username: str, password: str) -> str:
    is_username_exist = any(user[0].__eq__(username) for user in users)
    if is_username_exist:
        return 'bu kullanıcı adı alındı.'

    pwd_is_valid = is_pwd_valid(password=password)
    if pwd_is_valid:
        data = (username, password)
        users.append(data)
        return 'üyelik işlemi tamamlandı.'

    return 'yanlış parola girdiniz'

def is_pwd_valid(password: str) -> bool:
    char_set = set(password)

    is_result = (
        len(password) >= 16
        and any(c in string.ascii_uppercase for c in char_set)
        and any(c in string.ascii_lowercase for c in char_set)
        and any(c in string.digits for c in char_set)
        and any(c in string.punctuation for c in char_set)
    )

    return is_result

result = sign_up(username='berserk', password='fdasadf')
print(result)
print(users)