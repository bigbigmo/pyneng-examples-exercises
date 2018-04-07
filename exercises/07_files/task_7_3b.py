# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan_number = input('Input vlan number: ')

with open ('CAM_table.txt', 'r') as f:
    for line in f:
        line = line.split()
        if line == []:
            continue
        if line[0].isdigit() and line[0] == vlan_number:
            line.pop(2)
            line = "   ".join(line)
            print(line)
        else:
            continue
