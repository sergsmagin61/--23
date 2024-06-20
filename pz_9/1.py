'''
Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16', 
отражающая продажи продукции по дням в кг. Преобразовать информацию из 
строки в словари, с использованием функции найти среднее значение продаж по 
каждому виду продукции, результаты вывести на экран
'''


def count(data_string):
    w = data_string.split()
    #Создает словарь, где ключами являются виды продукции, а значениями - средние значения продаж.
    return {w[i]: sum(map(int, w[i + 1:i + 6])) / 5 
   
    for i in range(0, len(w), 6)}


raw_string = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'

# Вызываем функцию и выводим результаты
result = count(raw_string)
for p, a in result.items():
    print(f"Среднее продаж {p}: {a} кг")