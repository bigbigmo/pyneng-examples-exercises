# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
#преобразуем лист с исключениями
ignore = " ".join(ignore)
ignore = ignore.split()


file = input('Write name or path for file: ')

with open(file, 'r') as f:
    for line in f:
        if line.startswith('!'):
            continue
        #добавляем дополнительную проверку на пересечение со множеством исключений
        elif (set(line.split())).intersection(set(ignore)):
            continue
        else:
            print(line.strip('\n'))
