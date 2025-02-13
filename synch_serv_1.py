import requests
import time

source_serv = 'http://183.233.190.23:6060/GetDeviceList/100?UserName=200789'
filename = 'E:/python/_my.csv'
title = 'PlateNumber,DeviceId,ChannelNumber,DeviceType,GroupName \n'

if input('Синхронизируемый сервер 1 - 95.163.213.7, 2 - 37.139.33.129 \n')== '1':
    dest_serv = 'http://95.163.213.7:6060/GetDeviceList/100?UserName=admin'
else:
    dest_serv = 'http://37.139.33.129:6060/GetDeviceList/100?UserName=admin'

My_r = requests.get(dest_serv)
response = My_r.json()
print(f'Сервер {dest_serv} : {My_r.status_code} (200 - Ok)' )
MyDeviceList = response['DeviceList']

Stn_r = requests.get(source_serv)
response = Stn_r.json()
print(f'Сервер {source_serv} : {Stn_r.status_code} (200 - Ok)' )
StnDeviceList = response['DeviceList']

start_time = time.time()

NumMyDev =len(MyDeviceList)
NumStnDev =len(StnDeviceList)

My_file = open(filename, 'w')
My_file.write(title)

Numit = 0
k=0
for i in range (NumStnDev):
    not_incl = True
    for j in range(NumMyDev):
        Numit += 1
        if StnDeviceList[i]['DeviceId'] == (MyDeviceList[j]['DeviceId']):
            not_incl = False
            break
    if not_incl:
        k+=1
        add_dev = (str((StnDeviceList[i]['DeviceId'])) + ',' +str(StnDeviceList[i]['DeviceId']) + ',' +
                   str(StnDeviceList[i]['ChannelNumber'])+',' + str(StnDeviceList[i]['DeviceType']) +',visum \n')
        My_file.write(str(add_dev))

My_file.close()
end_time = time.time()
execution_time = end_time - start_time

print(f'Серв. источник: {NumStnDev}, синхр.сервер: {NumMyDev}, кол-во итераций {Numit}')
print(f"Время выполнения алг: {execution_time:.3f} с, добавлено {k} устройств в файл {filename}")
input('Нажмите Enter ')





