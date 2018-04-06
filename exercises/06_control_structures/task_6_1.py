# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_addr = input('Please enter your ip address in x.x.x.x format: ')
first_octet = ip_addr.split('.')

if int(first_octet[0]) in range (1,127):
    print('This is unicast ip. Class A')
elif int(first_octet[0]) in range (128,191):
    print('This is unicast ip. Class B')
elif int(first_octet[0]) in range (192,223):
    print('This is unicast ip. Class C')
elif int(first_octet[0]) in range (224,239):
    print('This is multicast ip')
elif ip_addr == '255.255.255.255':
    print('This is local broadcast ip')
elif int(first_octet[0]) == 0:
    print('Ip address in unassigned')
else:
    print('Ip in unused')
