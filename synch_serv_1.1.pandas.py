import requests
import time
import pandas as pd

source_serv = 'http://183.233.190.23:6060/GetDeviceList/100?UserName=200789'
dest_serv1 = 'http://95.163.213.7:6060/GetDeviceList/100?UserName=admin'
dest_serv2 = 'http://37.139.33.129:6060/GetDeviceList/100?UserName=admin'
filename = 'E:/python/_test.csv'
#filename_sourc = 'E:/python/_test2.csv'
#filename_dest = 'E:/python/_test3.csv'
title = 'PlateNumber,DeviceId,ChannelNumber,DeviceType,GroupName \n'

if input('Синхронизируемый сервер 1 - 95.163.213.7, 2 - 37.139.33.129 \n') == '1':
    dest_serv = dest_serv1
else:
    dest_serv = dest_serv2

My_r = requests.get(dest_serv)
print(f'Сервер {dest_serv} : {My_r.status_code} (200 - Ok)')
response = My_r.json()
MyDeviceList = response['DeviceList']

Stn_r = requests.get(source_serv)
print(f'Сервер {source_serv} : {Stn_r.status_code} (200 - Ok)')
response = Stn_r.json()
StnDeviceList = response['DeviceList']

start_time = time.time()

My=pd.DataFrame(MyDeviceList)
Stn=pd.DataFrame(StnDeviceList)
NumMyDev = len(My)
NumStnDev = len(Stn)

My_file = open(filename, 'w')
My_file.write(title)

el = 0
k = 0
while el < NumStnDev:
    if Stn['DeviceId'].values[el] not in My['DeviceId'].values:
        add_dev = (str((Stn['DeviceId'].values[el])) + ',' + str(Stn['DeviceId'].values[el]) + ',' +
                   str(Stn['ChannelNumber'].values[el]) + ',' + str(Stn['DeviceType'].values[el]) + ',visum \n')
        My_file.write(str(add_dev))
        k += 1
    el += 1

My_file.close()

end_time = time.time()
execution_time = end_time - start_time
print(f'Серв. источник: {NumStnDev}, синхр.сервер: {NumMyDev}')
print(f"Время выполнения алг: {execution_time:.3f} с, добавлено {k} устройств в файл {filename}")
input('Нажмите Enter ')
