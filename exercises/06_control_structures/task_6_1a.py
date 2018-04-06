# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


ip_addr = input('Please enter your ip address in x.x.x.x format: ')
ip_addr = ip_addr.split('.')


if len(ip_addr) != 4:
    print('Ip address must have 4 octets')

else:
    for i in ip_addr:
        if int(i) in range (0,255):
            first_octet = int(ip_addr[0])
        else:
            break


try:
    if first_octet in range (1,127):
        print('This is unicast ip. Class A')
    elif first_octet in range (128,191):
        print('This is unicast ip. Class B')
    elif first_octet in range (192,223):
        print('This is unicast ip. Class C')
    elif first_octet in range (224,239):
        print('This is multicast ip')
    elif ip_addr == '255.255.255.255':
        print('This is local broadcast ip')
    elif first_octet == 0:
        print('Ip address in unassigned')
    else:
        print('Ip in unused')

except:
    print("something wrong")
