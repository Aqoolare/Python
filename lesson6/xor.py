"""Скрипт реализующий XOR шифрование

Функции:
    xor_cipher(key, data='', encrypt=True): шифрует текст введённый 
    с клавиатуры, либо текст из файла
"""

def xor_cipher(key, data='', encrypt=True):
    """Шифрует текст введённый с клавиатуры, либо текст из файла
    и записывает результат в файл

    Аргументы:
        key (str): ключ шифрования
        data (str, optional): текст для шифрования. По умолчанию ''.
        encrypt (bool, optional): отвечает за то, какую операцию выполнить,
        шифровать текст введённый с клавиатуры (encrypt=True), либо шифровать 
        текст из файла (encrypt=False). По умолчанию True.
    """
    xored_text = bytearray()
    if encrypt:
        key = bytearray(key, 'utf-8')
        data = bytearray(data, 'utf-8')
        for i in range(len(data)):
            xored_text.append(data[i] ^ key[i % len(key)])
        write_bytes_to_file('lesson6/data.txt', xored_text)
        print('Текст зашифрован')
    else:
        f = open('lesson6/data.txt', 'rb')
        data = f.read()
        f.close()
        key = bytearray(key, 'utf-8')
        for i in range(len(data)):
            xored_text.append(data[i] ^ key[i % len(key)])
        write_bytes_to_file('lesson6/data.txt', xored_text)
        print(f'Шифрование произведено')


def write_bytes_to_file(filename, xored_text):
    """Записать текст в файл (в двоичном режиме)

    Аргументы:
        filename ([type]): имя файла
        xored_text ([type]): текст для записи в файл
    """
    f = open(filename,'wb')
    f.write(xored_text)
    f.close()


if __name__ == '__main__':
    while True:
        action = input('Выберите действие (зашифровать - 1, '
        'расшифровать(или зашифровать текст в файле) - 2, '
        'Enter - чтобы выйти): ')
        if action == '1':
            data = input('Введите текст:\n')
            key = input('Введите ключ:\n')
            xor_cipher(key, data)
        elif action == '2':
            key = input('Введите ключ:\n')
            xor_cipher(key,encrypt=False)
        elif action == '':
            break
        else:
            print('Пожалуйста, введите корректный код действия')

