"""
Напишите скрипт, который прочитает файл 2.txt
И создаст новый файл 2_raint.txt
И точно так же запишет тот же текст, заменив все слова дождь на ДОЖДЬ
(большими буквами)
Учитывая окончания, например  дожде -> ДОЖДЕ
"""
import re


def process_file(input_file: str, output_file: str) -> None:
    """
    Читает содержимое указанного файла, заменяет ключевые слова на верхний регистр
    с сохранением окончаний и записывает измененный текст в новый файл.

    nput_file: Имя исходного файла
    output_file: Имя файла, в который будет записан измененный текст
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
        # Используем регулярное выражение для замены ключевых слов на верхний регистр с сохранением окончаний
        modified_text = re.sub(r'\b(дожд[ьяюем]?)\b', lambda x: x.group(1).upper(), text)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(modified_text)


input_file = '2.txt'
output_file = '2_rain.txt'
process_file(input_file, output_file)


