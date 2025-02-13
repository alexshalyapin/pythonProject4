import requests

source_serv = 'http://183.233.190.23:6060/GetDeviceList/100?UserName=200789'
dest_serv = 'http://95.163.213.7:6060/GetDeviceList/100?UserName=admin'
#dest_serv = 'http://37.139.33.129:6060/GetDeviceList/100?UserName=admin'

filename = 'E:/python/_test.csv'
title = 'PlateNumber,DeviceId,ChannelNumber,DeviceType,GroupName \n'

My_r = requests.get(dest_serv)
response = My_r.json()
MyDeviceList = response['DeviceList']

Stn_r = requests.get(source_serv)
response = Stn_r.json()
StnDeviceList = response['DeviceList']

NumMyDev =len(MyDeviceList)
NumStnDev =len(StnDeviceList)

print(NumMyDev," ",NumStnDev)
Stn_list = list()
My_list = list()
#print(json.dumps(DeviceList, sort_keys=True, indent=4, ensure_ascii=False, separators=(",", ": ")))

for i in range (NumMyDev):
    My_list.append({(MyDeviceList[i]['DeviceId']) : (MyDeviceList[i]['DeviceType'])})

My_file = open(filename, 'w')
My_file.write(title)

k=0
for i in range (NumStnDev):
    not_incl = True
    for j in range(NumMyDev):
        if (StnDeviceList[i]['DeviceId'] == (MyDeviceList[j]['DeviceId'])):
            not_incl = False
            break
    if not_incl:
        k+=1
        add_dev = (str((StnDeviceList[i]['DeviceId'])) + ',' +str(StnDeviceList[i]['DeviceId']) + ',' +
                   str(StnDeviceList[i]['ChannelNumber'])+',' + str(StnDeviceList[i]['DeviceType']) +',visum \n')
        My_file.write(str(add_dev))
My_file.close()
print(k)


