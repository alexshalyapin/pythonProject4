import requests
import time
import pandas as pd

source_serv = 'http://183.233.190.23:6060/GetDeviceList/100?UserName=200789'
dest_serv1 = 'http://95.163.213.7:6060/GetDeviceList/100?UserName=admin'
dest_serv2 = 'http://37.139.33.129:6060/GetDeviceList/100?UserName=admin'
filename = 'E:/python/_test.csv'
filename2 = 'E:/python/export.csv'
filename3 = 'E:/python/res.csv'

def merge(Sort,p,q,r):
    n1 = q - p +1
    n2 = r-q

    Sort_lou = Sort[p:q+1]
    Sort_up = Sort[(q+1):r+1]
    Sort_lou._append({'DeviceId': float('inf')})
    Sort_up._append({'DeviceId': float('inf')})
    i = 0
    j = 0
    for k in range(p,r+1):
        if Sort_lou[i]['DeviceId']<=Sort_up[j]['DeviceId'] :
            print(Sort_lou[i]['DeviceId'], Sort_up[j]['DeviceId'])
            Sort[k]=Sort_lou[i]
            i+=1
        else:
            print(Sort_lou[i]['DeviceId'], Sort_up[j]['DeviceId'])
            Sort[k] = Sort_up[j]
            j+=1
    return Sort

def merge_sort(Sort,p,r):
    if p < r:
        q = (p+r)//2
        print(p, q, r)
        print(Sort)
        print('aaaaaaaaaaaaaaaaaaaaaaaaaa')
        print(Sort[p:q])
        print('bbbbbbbbbbbbbbbbbbbbbbbbb')
        print(Sort[(q):r])
        merge_sort(Sort, p,q)
        merge_sort(Sort, q+1,r)
        merge(Sort, p, q, r)
    else:
        print('last el')



My = pd.read_csv(filename, skiprows=0, sep=',', on_bad_lines='skip',
                    encoding='utf8')
NumMyDev =len(My)
My.drop([NumMyDev-1])# последняя строка всегда пустая/первая - заголовок
NumMyDev -= 1
print(NumMyDev)
merge_sort(My,0,NumMyDev)
My_res.to_csv(filename3, index=False)




