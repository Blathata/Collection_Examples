# номер посылки: 115277717
import re
from dataclasses import dataclass


@dataclass
class EncryptionData:
    """Декодирует, проверяет данные, используя специальные методы."""

    def validate_data(data: str) -> str:
        """ Метод проверяет корректность данных для расшифровки

        Args:
            data (str): Проверяемая строка

        Returns:
            str: Строка пройденая проверку на соответствие формату данных
        """

        if not isinstance(data, str):
            raise ValueError("Неправильный тип данных")
        if not re.findall(r'^[\d\w\[\]]{,30}$', data):
            raise ValueError("Неправильный формат вводимых данных")
        return data

    def decode_message(msg: str) -> str:
        """Метод расшифровки сжатых сообщений прошедших валидацию

        Args:
            msg(str): Строка содержащая только буквы, числа, квадратные скобки

        Returns:
            str: Возвращает строку с расшифроваными командами.
        """
        stack: list[tuple] = []
        multiplier: int = 0
        buffer_chars: str = ''
        sum_multiplier: str = ''
        for char in msg:
            if char == '[':
                stack.append((buffer_chars, multiplier))
                buffer_chars = ''
                multiplier = 0
                sum_multiplier = ''
            elif char == ']':
                prev_string, num = stack.pop()
                buffer_chars = prev_string + num * buffer_chars
            elif re.findall(r'[0-9]', char):
                sum_multiplier += char
                multiplier = int(sum_multiplier)
            else:
                buffer_chars += char
        return buffer_chars


def main():
    msg = '2[a3[xx2[yy]]]'
    verified_data = EncryptionData.validate_data(msg)
    decryption = EncryptionData.decode_message(verified_data)
    print(decryption)


if __name__ == '__main__':
    main()
