"""Скрипт для имитации работы светофора

Функции:
    traffic_lights(current_color): - выводит на экран
    реакцию на цвет 
"""

def traffic_lights(current_color):
    """Получает на выход название цвета,
    и по его значению выводит на экран 
    соотвествующую строку 

    Аргументы:
        current_color (str): название цвета светофора
    """
    if current_color == "red":
        print("Traffic is prohibited")
    elif current_color == "yellow":
        print("Attention")
    elif current_color == "green":
        print("Traffic allowed")
        

if __name__ == '__main__':
    current_condition = ""
    while current_condition != "exit":
        current_condition = input("Please, enter the color of "
        "the traffic light signal (red, yellow, green, exit - "
        "to exit the program)\n")
        traffic_lights(current_condition)