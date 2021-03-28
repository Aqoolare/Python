text = input("Введите текст:\n")
"""Анонимная функция для построения частотного словаря текста"""
freq_dict = dict(map(lambda symbol: (symbol, text.count(symbol)), set(text)))
print(freq_dict)