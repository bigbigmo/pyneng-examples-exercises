# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from __future__ import print_function, unicode_literals
from pprint import pprint

with open('ospf.txt', 'r') as f:

    for line in f:
        line = line.split()
        ospf_data = {}
        if line[0] == 'O':
            ospf_data.setdefault('Protocol', 'OSPF')
        else:
            print('This is not OSPF')
        ospf_data.setdefault('Prefix', line[1])
        ospf_data.setdefault('AD/Metric', line[2].strip('[]'))
        ospf_data.setdefault('Next-Hop', line[4].strip(','))
        ospf_data.setdefault('Last update', line[5].strip(','))
        ospf_data.setdefault('Outbound Interface', line[6])
        print(ospf_data)
