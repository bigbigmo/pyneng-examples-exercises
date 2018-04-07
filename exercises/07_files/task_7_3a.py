# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open ('CAM_table.txt', 'r') as f:
    mac_array = []
    for line in f:
        line = line.split()
        if line == []:
            continue
        if line[0].isdigit():
            line.pop(2)
            line = "   ".join(line)
            mac_array.append(line)
        else:
            continue
    mac_array.sort()
    print(mac_array)
