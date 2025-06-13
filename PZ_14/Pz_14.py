# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
# маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
# – все остальные. Посчитать количество полученных строк в каждом файле.

# import re
#
# with open('ip_address.txt', 'r') as file:
#     ip_addresses = file.readlines()
#
# ip_addresses = [ip.strip() for ip in ip_addresses] # Уб пробелы
#
# zero_octet = [] #для хранения
# non_zero_octet = []
#
# cocacola_zero = re.compile(r'\d+\.\d+\.\d+\.0$') #для нулевого
#
# for ip in ip_addresses:
#     if cocacola_zero.match(ip):
#         zero_octet.append(ip)
#     else:
#         non_zero_octet.append(ip)
#
# with open('z_octet_ips.txt', 'w') as file:
#     for ip in zero_octet:
#         file.write(ip + '\n')
#
#
# with open('non_octet_ips.txt', 'w') as file:
#     for ip in non_zero_octet:
#         file.write(ip + '\n')

# import re
#
# with open('ip_address.txt', 'r') as file:
#     ip_addresses = file.readlines()
#
# ip_addresses = [ip.strip() for ip in ip_addresses] #уд пробел
#
#
# zero_octet = []
# non_zero_octet = []
#
#
# zero_octet_p = re.compile(r'\d+\.\d+\.\d+\.0$') # для нулевого
# non_zero_octet_p = re.compile(r'\d+\.\d+\.\d+\.[1-9][0-9]?$') # для ненулевого
#
# # Разделение IP-адресов по условиям
# for ip in ip_addresses:
#     if zero_octet_p.match(ip):
#         zero_octet.append(ip)
#     elif non_zero_octet_p.match(ip):
#         non_zero_octet.append(ip)
#
# with open('z_octet_ips.txt', 'w') as file:
#     for ip in zero_octet:
#         file.write(ip + '\n')
#
# with open('non_octet_ips.txt', 'w') as file:
#     for ip in non_zero_octet:
#         file.write(ip + '\n')
#
#
# res_zero = len(zero_octet)
# res_non_zero = len(non_zero_octet)
# print(f"Количество строк с нулевым четвёртым октетом: {res_zero}")
# print(f"Количество строк с ненулевым четвёртым октетом: {res_non_zero}")

import re

with open('ip_address.txt', 'r') as file:
    ip_addresses = file.readlines()

ip_addresses = [ip.strip() for ip in ip_addresses] #уд пробелов

zero_octet = []
non_zero_octet = []

zero_octet_p = re.compile(r'\d+\.\d+\.\d+\.0$') # для нулевого, компилирует строку в объект
non_zero_octet_p = re.compile(r'\d+\.\d+\.\d+\.[1-9]\d{0,2}$') # для ненулевого

for ip in ip_addresses:
    if zero_octet_p.match(ip):
        zero_octet.append(ip)
    elif non_zero_octet_p.match(ip):
        non_zero_octet.append(ip)

with open('z_octet_ips.txt', 'w') as file:
    for ip in zero_octet:
        file.write(ip + '\n')

with open('non_octet_ips.txt', 'w') as file:
    for ip in non_zero_octet:
        file.write(ip + '\n')

res_zero = len(zero_octet)
res_non_zero = len(non_zero_octet)
print(f"Количество строк с нулевым четвёртым октетом: {res_zero}")
print(f"Количество строк с ненулевым четвёртым октетом: {res_non_zero}")

