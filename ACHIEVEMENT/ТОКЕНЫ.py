# JWT токен
import jwt
import random
import string

# генерация секретного ключа из рандомных чисел и букв, длиной в 16 символов
secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# пример данных пользователя (payload)
payload = {'username': 'REST API', 'email': 'Best@Course.com'}

# генерация токена, с использование алгоритма шифрования HS256
token = jwt.encode(payload, secret_key, algorithm='HS256')
print('--------------------------------')
print(f'Ваш токен: {token}')
print(f'Ваш секретный ключ: {secret_key}')


# Basic token

import base64
# входные данные
username = 'David'
password = 'SlozhniyParol:)'

# объединение username и password и кодировка в base64
token = base64.b64encode(f'{username}:{password}'.encode())

print(f'Ваш токен: {token.decode()}')

# украли токен и проводим расшифровку токена
token = 'RGF2aWQ6U2xvemhuaXlQYXJvbDop'
decoded_token = base64.b64decode(token)

print(f'Расшифровка токена: {decoded_token.decode()}')