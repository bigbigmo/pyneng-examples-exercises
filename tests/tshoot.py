from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from getpass import getpass

try:
    host =  raw_input("Enter host to connect to: ")
except:
    host = input("Enter host to connect to: ")

password = getpass()

cisco3725 = {
    'device_type': 'cisco_ios',
    'ip': host,
    'username': 'cisco',
    'password': password
}

command = 'show ip int br'

net_connect = ConnectHandler(**cisco3725)
print(net_connect.find_prompt())
output = net_connect.send_command(command)

print(output)
