# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
#преобразуем лист с исключениями
ignore = " ".join(ignore)
ignore = ignore.split()


file = input('Write name or path for file: ')

with open(file, 'r') as src, open('config_sw1_cleared.txt', 'w') as dest:
    for line in src:
        if (set(line.split())).intersection(set(ignore)):
            continue
        else:
            dest.write(line)
