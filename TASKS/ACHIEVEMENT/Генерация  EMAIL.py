from random import randint
from string import ascii_lowercase, digits, ascii_uppercase

EMAIL_RANDOM_CHARS = ascii_lowercase + digits + ascii_uppercase + '_'

def get_random_email(cls):
    n = randint(4,20)
    length = len(cls.EMAIL_RANDOM_CHARS) - 1
    return ''.join(cls.EMAIL_RANDOM_CHARS[randint(0, length)] for i in range(n)) + '@gmail.com'