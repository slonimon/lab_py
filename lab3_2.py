# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, symboll=","):
    first_group_list = first_group.split(symboll)
    second_group_list = second_group.split(symboll)
    first_group_set = set(first_group_list)
    second_group_set = set(second_group_list)
    intersection_group = first_group_set.intersection(second_group_set)
    intersection_group_sort = sorted(list(intersection_group))
    return intersection_group_sort

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group))
