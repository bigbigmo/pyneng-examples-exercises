# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import re
full_network = input('Please input your network in standard format: ')
full_network = full_network.replace('/', '.')
full_network = list(map(int, full_network.split('.')))

network = full_network[:4]
mask = full_network[4:]

print('Network:')
for i in network:
    print('{:<10}'. format(i), end='')
print()
for i in network:
    print('{:<10}'.format(bin(i)[2:].zfill(8)), end='')

print()
print('Mask:')
for i in mask:
    print('{:<10}'. format(i), end='')
print()
for i in mask:
    print('{:<10}'.format(bin(i)[2:].zfill(8)), end='')
