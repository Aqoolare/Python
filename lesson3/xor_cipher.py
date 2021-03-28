"""Скрипт для выполнения XOR шифрования

Функции:
    xor_cipher(data, key, decrypt=False): шифрование через консоль
    xor_cipher_in_file(file_name): шифрование в файл
"""

import base64
import json


def xor_cipher(data, key, decrypt=False):
    """Шифрует и расшифровывает строку с помощью xor шифрования
    по ключу, возвращает результат

    Аргументы:
        data (str): строка для шифрования/расшифровки
        key (str): ключ шифрования
        decrypt (bool, optional): ключ, указывающий какое действие необходимо
        произвести со строкой (расшифовать или зашифровать). 
        По умолчанию False.

    Возвращает:
        str: строка - результат шифрования
    """
    result = []
    if decrypt:
        data = data.encode('utf-8')
        data = base64.b64decode(data)
        data = data.decode('utf-8')
    for i in range(len(data)):
        result.append(chr(ord(data[i]) ^ ord(key[i % len(key)])))
    result = ''.join(result).encode('utf-8')
    if not decrypt:
        return base64.b64encode(result).decode('utf-8')
    return result.decode('utf-8')

def xor_cipher_in_file(file_name):
    """Шифрует и расшифровывает строку из файла с помощью xor шифрования
    по ключу, результат записывает в формате json в файл

    Args:
        file_name (str): имя файла с парой текст: ключ 
    """
    xored_text = []
    f = open(file_name)
    file_data = f.read()
    json_data = json.loads(file_data)
    for i in range(len(json_data['data'])):
        xored_text.append(chr(ord(json_data['data'][i]) ^ 
        ord(json_data['key'][i % len(json_data['key'])])))
    xored_text = ''.join(xored_text)
    result = {"key": json_data['key'], "data": xored_text}
    json_data = json.dumps(result)
    f = open(file_name,'w')
    f.write(json_data)
    f.close()


if __name__ == '__main__':
    # data = {'key': 'It is a key!', 'data': 'It is a data!'}
    # json_data = json.dumps(data)
    # f = open('lesson3/file_data.txt', 'w')
    # f.write(json_data)
    # f.close()
    xor_cipher_in_file('lesson3/file_data.txt')

    data = input("Введите сообщение: ")
    key = input("Введите ключ: ")
    result = xor_cipher(data, key)
    print(f"Зашифрованный текст: {result}")
    print(f"Расшифрованный текст: {xor_cipher(result, key, True)}")