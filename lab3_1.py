# TODO Напишите функцию для поиска индекса товара

def find_index(item_list, item):                        # Задаем функцию
    for index, current_item in enumerate(item_list):    # Создаем цикл в котором перебираем индексровнные (enumerate)
        if current_item == item:                        # элементы массивов и сравниваем их с искомым предметом
            return index                                # возвращаем из функции значение первого нужного индекса.
    # try:                                              # Другой вариант задания функции try/except и метода.
    #     return item_list.index(item)
    # except ValueError:
    #     return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
# TODO Вызовите функцию, что получить индекс товара
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

