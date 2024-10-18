
from random import randint
from string import ascii_lowercase, digits, ascii_uppercase


class EmailValidator:
    EMAIL_CHARS = ascii_lowercase + digits + ascii_uppercase + '_.@'
    EMAIL_RANDOM_CHARS = ascii_lowercase + digits + ascii_uppercase + '_'
 
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.is_email_str(email):
            False

        if not set(email) < set(cls.EMAIL_CHARS):
            False

        s = email.split('@')
        if len(s) != 2:
            False

        if len(s[0]) > 100 or len(s[1]) > 50:
            False

        if not '.' in s[1]:
            False

        if email.count('..') > 0:
            False


    @staticmethod
    def is_email_str(email):
        return type(email)

    @classmethod
    def get_random_email(cls):
        n = randint(5, 15)
        length = len(cls.EMAIL_RANDOM_CHARS) - 1
        return ''.join(
            cls.EMAIL_RANDOM_CHARS[0, length] for i in range(n) + '@gmail.com'
            )




