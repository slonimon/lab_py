# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    #TODO считать содержимое csv файла
    in_data = []
    with open(INPUT_FILENAME, 'r') as file_c:
        reader = csv.DictReader(file_c)
        for row in reader:
            in_data.append(row)

# В отличие от csv.reader, где каждая строка возвращается в виде списка значений,
# DictReader возвращает каждую строку в виде словаря, где ключами являются
# значения первой строки (заголовка), а значениями - соответствующие значения в
# текущей строке.

    #TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as file_j:
        json.dump(in_data, file_j, indent=4, ensure_ascii=True)     # Метод dump позволяет сериализовать данные и записать их в файловый объект.
        # Аргумент indent используется для задания количества пробелов,
        # используемых для отступов в форматированном JSON.

        # ensure_ascii равно True, что означает, что все не-ASCII символы
        # будут преобразованы в escape-последовательности.

if __name__ == '__main__':
# Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
