# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

"""interface FastEthernet1/1
 switchport mode access
 switchport access vlan 30
 duplex auto
!
interface FastEthernet1/2
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 400,500
 switchport mode trunk
 duplex auto"""

def get_int_vlan_map(conf):
    trunk_ports = {}
    access_ports = {}
    with open (conf) as f:
        ports = []
        new_ports = []
        for line in f.readlines():
            if line.startswith (('interface F', 'interface G', ' switchport trunk allowed', ' switchport access')):
                ports.append(line.rstrip())
            elif  line.startswith('!'):
                pass

        for a,b in zip(ports[0::2], ports[1::2]):
            new_ports.append(a+b)

    print(new_ports)

get_int_vlan_map('config_sw1.txt')
